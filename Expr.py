from Tokenizer import TokList
from Term import Term
class Expr:
    def __init__(self):
        self.term = None
        self.expr = None
        self.plusOrMinus = ''
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
    def print(self):
        self.term.print()
        if '+' in self.plusOrMinus:
            print(self.plusOrMinus, end='')
            self.expr.print()
        elif '-' in self.plusOrMinus:
            print(self.plusOrMinus, end='')
            self.expr.print()
    def exec(self):
        if not self.plusOrMinus:
            return self.term.exec()
        elif '+' in self.plusOrMinus:
            return self.term.exec() + self.expr.exec()
        elif '-' in self.plusOrMinus:
            return self.term.exec() - self.expr.exec()
        return 0