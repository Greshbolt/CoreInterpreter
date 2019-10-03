import scanner
class Tokenizer:
    def __init__(self):
        self.pointer = 0
        self.dataPointer = 0
        self.dataList = []
        self.tokenList = []
        self.idDict = {}
        self.indentAmount = 0
    def printIndent(self):
        for x in range(self.indentAmount):
            print(end='  ')
    def increaseIndent(self):
        self.indentAmount+=1
    def decreaseIndent(self):
        self.indentAmount-=1
    def getFiles(self, code, data):
        s = scanner.Scanner(code,data)
        self.tokenList = s.generateTokenList()
        self.idDict = s.idDict
        self.dataList = s.generateDataList()
    def getIdOrConst(self):
        if 'ID' in self.tokenList[self.pointer] or 'CONST' in self.tokenList[self.pointer]:
            return self.tokenList[self.pointer][self.tokenList[self.pointer].find('[')+1:self.tokenList[self.pointer].find(']')]
        print('ERROR: improper syntax')
        exit()
    def getIdValue(self, idName):
        return self.idDict[str(idName)]
    def setIdValue(self, idName, value):
        self.idDict[str(idName)] = value
    def nextData(self):
        self.dataPointer+=1
        if self.dataPointer > len(self.dataList):
            print('ERROR: unexpected end of data file')
            exit()
    def currentData(self):
        return self.dataList[self.dataPointer]
    def nextToken(self):
        self.pointer+=1
        if self.pointer > len(self.tokenList)-1:
            print('ERROR: unexpected end of file')
            exit()
    def currentToken(self):
        return self.tokenList[self.pointer]
    def checkTok(self, token):
        if token == 'ID' or token == 'CONST':
            return (token in self.tokenList[self.pointer])
        return (token == self.tokenList[self.pointer])
    def match(self, token, location):
        if 'EOF' == self.currentToken():
            print('ERROR: Unexpected End Of File occured at: ' + location)
            exit()
        if(token == self.tokenList[self.pointer]):
            self.nextToken()
            return True
        print("ERROR: Syntax error in: " + location)
        exit()
TokList = Tokenizer()


