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
    def currentToken(self):
        return self.tokenList[self.pointer]
TokList = Tokenizer()


