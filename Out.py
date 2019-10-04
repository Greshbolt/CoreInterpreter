from Tokenizer import TokList
from Expr import Expr
class Out:
    def __init__(self):
        self.expr = None
    #Simple parsing for output statement
    def parse(self):
        TokList.match('OUTPUT', 'output')
        self.expr = Expr()
        self.expr.parse()
        TokList.match('SEMICOLON', 'output')
    #Simple printing
    def print(self):
        TokList.printIndent()
        print('output ', end='')
        self.expr.print()
        print(';')
    #Execution that prints the values returned by the expression evaluation
    def exec(self):
        print(self.expr.exec())