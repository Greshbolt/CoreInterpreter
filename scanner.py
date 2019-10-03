import sys
class Scanner:
    def __init__(self, codeFile, dataFile):
        self.code = codeFile
        self.data = dataFile
        self.tokenList = []
        self.idDict = {}
        self.symbols = [',',';','!','(',')','=','+','-','*']
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
    def TokenGenerator(self, tokenString):
        token = [self.tokenSwitcher.get(tokenString,"n/a")]
        if token[0] == 'n/a' and tokenString.isnumeric():
            token = [f'CONST[{tokenString}]']
        elif token[0] == 'n/a' and not tokenString[0].isnumeric() and tokenString.isalnum():
            token = [f'ID[{tokenString}]']
            self.idDict[str(tokenString)] = 'null'
        elif token[0] == 'n/a':
            token = self.checkForKeyword(tokenString)
        return token
    def checkForKeyword(self, tokenString):
        token = []
        if len(tokenString) == 0 :
            return token
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
                self.idDict[str(temptok)] = 'null'
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
    def generateDataList(self):
        data=open(f'{self.data}','r')
        dataContents = data.read()
        dataContentsSplit = dataContents.split()
        if not any(dat.isnumeric() for dat in dataContentsSplit):
            print('ERROR: Data file is corrupt')
        data.close()
        return dataContentsSplit
    def generateTokenList(self):
        code=open(f'{self.code}','r')
        codeContents = code.read()
        codeContentsSplit = codeContents.split()
        codeContentsSplit.append('EOF')
        scannerList = []
        for token in codeContentsSplit:
            temp = self.TokenGenerator(token)
            scannerList.extend(temp)
        self.tokenList = scannerList
        code.close()
        return self.tokenList
   



