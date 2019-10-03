from Tokenizer import TokList
from Const import Const
from ConstList import ConstList
from Expr import Expr
from CaseLineFollow import CaseLineFollow
class CaseLine:
    def __init__(self):
        self.const = None
        self.constList = None
        self.expr = None
        self.caseLineFollow = None
    def parse(self):
        self.const = Const()
        self.const.parse(TokList.getIdOrConst())
        TokList.nextToken()
        if TokList.currentToken() == 'COMMA':
            self.constList = ConstList()
            self.constList.parse()
        TokList.match('COLON','case line')
        self.expr = Expr()
        self.expr.parse()
        self.caseLineFollow = CaseLineFollow()
        self.caseLineFollow.parse()
    def print(self):

        self.const.print()
        if self.constList is not None:
            self.constList.print()
        print(':', end='')
        self.expr.print()
        self.caseLineFollow.print()
    def exec(self, caseId):
        if self.const.exec() == caseId.getValue():
            caseId.setValue(self.expr.exec())
            return True
        if self.constList is not None:
            if self.constList.exec(caseId):
                caseId.setValue(self.expr.exec())
                return True
        if self.caseLineFollow.exec(caseId):
            return True
        return False
