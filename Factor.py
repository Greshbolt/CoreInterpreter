from Tokenizer import TokList
from Const import Const
from Id import Id
import Expr
class Factor:
    def __init__(self):
        self.const = None
        self.id = None
        self.expr = None
    def parse(self):
        if TokList.checkTok('CONST'):
            self.const = Const()
            self.const.parse(TokList.getIdOrConst())
            TokList.nextToken()
        elif TokList.checkTok('ID'):
            self.id = Id()
            self.id.parse(TokList.getIdOrConst())
            TokList.nextToken()
        elif TokList.match('LEFTPARAN', 'factor'):
            TokList.nextToken()
            self.expr = Expr.Expr()
            self.expr.parse()
            TokList.match('RIGHTPARAN', 'factor')
    def print(self):
        if self.const is not None:
            self.const.print()
        elif self.id is not None:
            self.id.print()
        elif self.expr is not None:
            self.expr.print()
    def exec(self):
        if self.const is not None:
            return self.const.exec()
        elif self.id is not None:
            return self.id.getValue()
        elif self.expr is not None:
            return self.expr.exec()