import scanner
#This is used as a global class for all the files to iterate through the list of tokens generated by the scanner
class Tokenizer:
    def __init__(self):
        self.pointer = 0
        self.dataPointer = 0
        self.dataList = []
        self.tokenList = []
        self.idDict = {}
        self.indentAmount = 0
    #Used for printing indentation
    def printIndent(self):
        for x in range(self.indentAmount):
            print(end='  ')
    #Increasing indentation
    def increaseIndent(self):
        self.indentAmount+=1
    #Decreasing indentation
    def decreaseIndent(self):
        self.indentAmount-=1
    #Acquires the files and generates appropriate lists
    def getFiles(self, code, data):
        s = scanner.Scanner(code,data)
        self.tokenList = s.generateTokenList()
        self.idDict = s.idDict
        self.dataList = s.generateDataList()
    #Gets the name of an Id or the value of a const
    def getIdOrConst(self):
        if 'ID' in self.tokenList[self.pointer] or 'CONST' in self.tokenList[self.pointer]:
            return self.tokenList[self.pointer][self.tokenList[self.pointer].find('[')+1:self.tokenList[self.pointer].find(']')]
        print('ERROR: improper syntax')
        exit()
    #Gets value of id from map
    def getIdValue(self, idName):
        return self.idDict[str(idName)]
    #Sets value of id from map
    def setIdValue(self, idName, value):
        self.idDict[str(idName)] = value
    #Checks if the id is already in the Dictionary
    def checkId(self, idName):
        return idName in self.idDict
    #Iterates to the next data value
    def nextData(self):
        self.dataPointer+=1
    #Returns the current data value
    def currentData(self):
        if self.dataPointer >= len(self.dataList):
            print('ERROR: unexpected end of data file')
            exit()
        return self.dataList[self.dataPointer]
    #Iterates to the next token
    def nextToken(self):
        self.pointer+=1
        if self.pointer > len(self.tokenList)-1:
            print('ERROR: unexpected end of file')
            exit()
    #Returns the current token
    def currentToken(self):
        return self.tokenList[self.pointer]
    #Returns if the current token is the value passed in
    def checkTok(self, token):
        if token == 'ID' or token == 'CONST':
            return (token in self.tokenList[self.pointer])
        return (token == self.tokenList[self.pointer])
    #If the current token is the one passed in it iterates to the next otherwise outputs an error
    def match(self, token, location):
        if 'EOF' == self.currentToken():
            print('ERROR: Unexpected End Of File occured')
            exit()
        if(token == self.tokenList[self.pointer]):
            self.nextToken()
            return True
        print("ERROR: Syntax error in: " + location)
        exit()
#Initialized a global variable for uses
TokList = Tokenizer()


