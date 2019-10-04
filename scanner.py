class Scanner:
    def __init__(self, codeFile, dataFile):
        self.code = codeFile
        self.data = dataFile
        self.tokenList = []
        self.idDict = {}
        #Symbols for long string parsing
        self.symbols = [',',';','!','(',')','=','+','-','*','|']
        #Keywords to tokens dictionary
        self.tokenSwitcher = {
            'program': 'PROGRAM',
            'begin': 'BEGIN',
            'int': 'INT',
            'input': 'INPUT',
            'case': 'CASE', 
            'of': 'OF',
            'else': 'ELSE',
            'end': 'END',
            'if': 'IF',
            'then': 'THEN',
            'endif': 'ENDIF',
            'while':'WHILE',
            'endwhile': 'ENDWHILE',
            'or': 'OR',
            'output':'OUTPUT',
            'EOF': 'EOF',
            ':=': 'ASSIGN',
            ':' : 'COLON',
            ';': 'SEMICOLON',
            ',': 'COMMA',
            '|': 'BAR',
            '!': 'NOT',
            '(': 'LEFTPARAN',
            ')': 'RIGHTPARAN',
            '=': 'EQUAL',
            '<': 'LESSTHAN',
            '<=': 'LESSTHANEQUAL',
            '+': 'PLUS',
            '-': 'MINUS',
            '*': 'MULT',
        }
    #This is used to generate the tokens using the keyword dictionary
    #It checks whether something is a keyword, otherwise it is a const, id, or longer string
    def TokenGenerator(self, tokenString):
        token = [self.tokenSwitcher.get(tokenString,"n/a")]
        if token[0] == 'n/a' and tokenString.isnumeric():
            token = [f'CONST[{tokenString}]']
        elif token[0] == 'n/a' and not tokenString[0].isnumeric() and tokenString.isalnum():
            token = [f'ID[{tokenString}]']
            #Adds any Ids that it finds into a dictionary initialized as none for future use
            self.idDict[str(tokenString)] = None
        elif token[0] == 'n/a':
            token = self.checkForKeyword(tokenString)
        return token
    #This is what parses the longer strings into either tokens for keywords, ids, constants, or improper syntax
    def checkForKeyword(self, tokenString):
        token = []
        #For recursive exiting
        if len(tokenString) == 0 :
            return token
        #Where all the checking and recursive calls occur.  Follows algorithm in slides
        if tokenString[0] in self.symbols:
            token = self.TokenGenerator(tokenString[0])
            token.extend(self.checkForKeyword(tokenString[1:]))
        elif tokenString[0] == ':':
            if len(tokenString) == 1 or tokenString[1] != '=':
                print('ERROR: improper syntax for COLON')
                exit()
            elif tokenString[1] == '=':
                token = self.TokenGenerator(':=')
                token.extend(self.checkForKeyword(tokenString[2:]))
        elif tokenString[0] == '<':
            if len(tokenString) == 1 or tokenString[1] != '=':
                token = self.TokenGenerator('<')
                token.extend(self.checkForKeyword(tokenString[1:]))
            elif tokenString[1] == '=':
                token = self.TokenGenerator('<=')
                token.extend(self.checkForKeyword(tokenString[2:]))
        elif tokenString[0].isalpha():
            temptok = ''
            counter = 0
            for x in tokenString:
                if not x.isalnum():
                    break
                temptok = temptok+x
                counter+=1
            if self.tokenSwitcher.get(temptok,'n/a') == 'n/a':
                #Adds any Ids that it finds into a dictionary initialized as none for future use
                self.idDict[str(temptok)] = None
                token.append(f'ID[{temptok}]')
                token.extend(self.checkForKeyword(tokenString[counter:]))
            else:
                token.append(self.tokenSwitcher.get(temptok,'n/a'))
                token.extend(self.checkForKeyword(tokenString[counter:]))
        elif tokenString[0].isnumeric():
            temptok = ''
            counter = 0
            for x in tokenString:
                if not x.isnumeric():
                    break
                temptok = temptok+x
                counter+=1
            token.append(f'CONST[{temptok}]')
            token.extend(self.checkForKeyword(tokenString[counter:]))
        else:
            print('ERROR: Unknown format')
            exit()
        return token
    #Used for checking if numbers are ints
    def representsInt(self, s):
        if s[0] == '-':
            return s[1:].isnumeric()
        return s.isnumeric()
    #Used to generate the Data List
    def generateDataList(self):
        #Opens data file for reading
        data=open(f'{self.data}','r')
        dataContents = data.read()
        #Splits whitespace for just tokens
        dataContentsSplit = dataContents.split()
        dataList = []
        #Iterates through data file to search for non integers
        for dat in dataContentsSplit:
            if not self.representsInt(dat):
                print('ERROR: Data file is corrupt')
                exit()
            dataList.append(int(dat))
        data.close()
        return dataList
    #Used to generate the token list
    def generateTokenList(self):
        #Opens code file for reading
        code=open(f'{self.code}','r')
        codeContents = code.read()
        codeContentsSplit = codeContents.split()
        #Adds EOF to end of split
        codeContentsSplit.append('EOF')
        scannerList = []
        #Iterates through code file to create tokens
        for token in codeContentsSplit:
            temp = self.TokenGenerator(token)
            scannerList.extend(temp)
        self.tokenList = scannerList
        code.close()
        return self.tokenList
   



