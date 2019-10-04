from Tokenizer import TokList
from Term import Term
class Expr:
    def __init__(self):
        self.term = None
        self.expr = None
        self.plusOrMinus = ''
    #Parsing for Expression that checks for plus, minus, or no calculations
    def parse(self):
        self.term = Term()
        self.term.parse()
        if TokList.checkTok('PLUS'):
            TokList.nextToken()
            self.plusOrMinus = '+'
            self.expr = Expr()
            self.expr.parse()
        elif TokList.checkTok('MINUS'):
            TokList.nextToken()
            self.plusOrMinus = '-'
            self.expr = Expr()
            self.expr.parse()
    #Simple print statement
    def print(self):
        self.term.print()
        if '+' in self.plusOrMinus:
            print(self.plusOrMinus, end='')
            self.expr.print()
        elif '-' in self.plusOrMinus:
            print(self.plusOrMinus, end='')
            self.expr.print()
    #Simple execute statement that returns a value based on parsing
    def exec(self):
        if not self.plusOrMinus:
            return self.term.exec()
        elif '+' in self.plusOrMinus:
            return self.term.exec() + self.expr.exec()
        elif '-' in self.plusOrMinus:
            return self.term.exec() - self.expr.exec()