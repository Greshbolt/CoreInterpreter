from Tokenizer import TokList
from Expr import Expr
class Out:
    def __init__(self):
        self.expr = None
    def parse(self):
        TokList.match('OUTPUT', 'output')
        self.expr = Expr()
        self.expr.parse()
        TokList.match('SEMICOLON', 'output')
    def print(self):
        TokList.printIndent()
        print('output ', end='')
        self.expr.print()
        print(';')
    def exec(self):
        print(self.expr.exec())