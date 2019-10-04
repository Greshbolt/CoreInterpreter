from Tokenizer import TokList
from Id import Id
from Expr import Expr
class Assign:
    def __init__(self):
        self.id = None
        self.expr = None
    #Simple parsing for Assign
    def parse(self):
        self.id = Id()
        self.id.parse(TokList.getIdOrConst())
        TokList.nextToken()
        TokList.match('ASSIGN','assign')
        self.expr = Expr()
        self.expr.parse()
        TokList.match('SEMICOLON','assign')
    #Simple printing for Assign
    def print(self):
        TokList.printIndent()
        self.id.print()
        print(':=',end='')
        self.expr.print()
        print(';')
    #Executor that determines value of an expression and then sets that value to the respective Id
    def exec(self):
        val = self.expr.exec()
        self.id.setValue(val)
