from Tokenizer import TokList
from Const import Const
class ConstList:
    def __init__(self):
        self.const = None
        self.constList = None
    def parse(self):
        TokList.nextToken()
        self.const = Const()
        self.const.parse(TokList.getIdOrConst())
        TokList.nextToken()
        if TokList.currentToken() == 'COMMA':
            self.constList = ConstList()
            self.constList.parse()
    def print(self):
        print(', ')
        self.const.print()
        if self.constList is not None:
            self.constList.print()
    def exec(self, caseId):
        if self.const.exec() == caseId.getValue():
            return True
        if self.constList is not None:
            return self.constList.exec(caseId)
        return False