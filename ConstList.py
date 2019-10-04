from Tokenizer import TokList
from Const import Const
class ConstList:
    def __init__(self):
        self.const = None
        self.constList = None
    #Parsing to determine the amount of constants to compare to the id in the constat list
    def parse(self):
        TokList.nextToken()
        self.const = Const()
        self.const.parse(TokList.getIdOrConst())
        TokList.nextToken()
        if TokList.currentToken() == 'COMMA':
            self.constList = ConstList()
            self.constList.parse()
    #Simple print
    def print(self):
        print(',', end='')
        self.const.print()
        if self.constList is not None:
            self.constList.print()
    #Recursive executor that runs through all constant values in the constant list to compare to id
    def exec(self, caseId):
        if self.const.exec() == caseId.getValue():
            return True
        if self.constList is not None:
            return self.constList.exec(caseId)
        return False