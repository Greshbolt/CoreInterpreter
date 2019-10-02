import sys
class Scanner:
    symbols = [':=',':',',',';','|','!','(',')','=','<','<=','+','-','*']
    def __init__(self, codeFile, dataFile):
        self.code = codeFile
        self.data = dataFile
        self.tokenList = []
        self.idDict = {}
    def TokenGenerator(self, tokenString):
        tokenSwitcher = {
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
        token = tokenSwitcher.get(tokenString,"n/a")
        if token == 'n/a' and tokenString.isnumeric():
            token = f'CONST[{tokenString}]'
        elif token == 'n/a' and not tokenString[0].isnumeric() and tokenString.isalnum():
            token = f'ID[{tokenString}]'
            self.idDict[tokenString] = 'null'
        elif token == 'n/a':
            token = 'ERROR: improper syntax'
        return token
    def generateTokenList(self):
        code=open(f'{self.code}','r')
        data=open(f'{self.data}','r')
        codeContents = code.read()
        dataContents = data.read()
        codeContentsSplit = codeContents.split()
        dataContentsSplit = dataContents.split()
        codeContentsSplit.append('EOF')
        scannerList = []
        for token in codeContentsSplit:
            temp = self.TokenGenerator(token)
            if "ERROR" in temp:
                print(temp)
                break
            scannerList.append(temp)
        self.tokenList = scannerList
        code.close()
        data.close()
        return self.tokenList
   



