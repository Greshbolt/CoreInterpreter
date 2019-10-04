from Tokenizer import TokList
from Const import Const
from Id import Id
import Expr
class Factor:
    def __init__(self):
        self.const = None
        self.id = None
        self.expr = None
    #Simple parsing that checks for constant, Id, or paranthesis
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
            self.expr = Expr.Expr()
            self.expr.parse()
            TokList.match('RIGHTPARAN', 'factor')
    #Simple print statement
    def print(self):
        if self.const is not None:
            self.const.print()
        elif self.id is not None:
            self.id.print()
        elif self.expr is not None:
            print('(', end='')
            self.expr.print()
            print(')', end='')
    #Simple execution statement that returns a value based on parsing
    def exec(self):
        if self.const is not None:
            return self.const.exec()
        elif self.id is not None:
            return self.id.exec()
        elif self.expr is not None:
            return self.expr.exec()