import scanner
class Tokenizer:
    def __init__(self):
        self.pointer = 0
        self.tokenList = []
        self.idDict = {}
    def getFiles(self, code, data):
        s = scanner.Scanner(code,data)
        self.idDict = s.idDict
        self.tokenList = s.generateTokenList()
    def nextToken(self):
        self.pointer+=1
        if self.pointer > len(self.tokenList)-1:
            print('ERROR: unexpected end of file')
            exit()
    def currentToken(self):
        return self.tokenList[self.pointer]
    def checkTok(self, token):
        return (token in self.tokenList[self.pointer])
    def match(self, token):
        if(token in self.tokenList[self.pointer]):
            self.nextToken()
            return
        print("ERROR: Syntax error")
        exit()
TokList = Tokenizer()


