from Tokenizer import TokList
from Expr import Expr
class Cmpr:
    def __init__(self):
        self.rightExpr = None
        self.leftExpr = None
        self.checkValue = None
    def parse(self):
        self.leftExpr = Expr()
        self.leftExpr.parse()
        if TokList.checkTok('EQUAL'):
            self.checkValue = '='
            TokList.nextToken()
        elif TokList.checkTok('LESSTHAN'):
            self.checkValue = '<'
            TokList.nextToken()
        elif TokList.checkTok('LESSTHANEQUAL'):
            self.checkValue = '<='
            TokList.nextToken()
        else:
            print('Error: improper syntax for comparator')
            exit()
        self.rightExpr = Expr()
        self.rightExpr.parse()
    def print(self):
        self.leftExpr.print()
        print(self.checkValue, end='')
        self.rightExpr.print()
    def exec(self):
        if self.checkValue == '=':
            return self.leftExpr.exec() == self.rightExpr.exec()
        elif self.checkValue == '<':
            return self.leftExpr.exec() < self.rightExpr.exec()
        elif self.checkValue == '<=':
            return self.leftExpr.exec() <= self.rightExpr.exec()
