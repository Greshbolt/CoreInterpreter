from Tokenizer import TokList
from Id import Id
from Expr import Expr
class Assign:
    def __init__(self):
        self.id = None
        self.expr = None
    def parse(self):
        self.id = Id()
        self.id.parse(TokList.getIdOrConst())
        TokList.nextToken()
        TokList.match('ASSIGN','assign')
        self.expr = Expr()
        self.expr.parse()
        TokList.match('SEMICOLON','assign')
    def print(self):
        TokList.printIndent()
        self.id.print()
        print(':=',end='')
        self.expr.print()
        print(';')
    def exec(self):
        val = self.expr.exec()
        self.id.setValue(val)
