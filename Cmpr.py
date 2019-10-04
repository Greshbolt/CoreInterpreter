from Tokenizer import TokList
from Expr import Expr
class Cmpr:
    def __init__(self):
        self.rightExpr = None
        self.leftExpr = None
        self.checkValue = None
    #Parsing to determine kind of comparator.  Checks for middle comparison while returning an error if none are given.
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
    #Simple printing
    def print(self):
        self.leftExpr.print()
        print(self.checkValue, end='')
        self.rightExpr.print()
    #Executor based on results gained while parsing
    def exec(self):
        if self.checkValue == '=':
            return self.leftExpr.exec() == self.rightExpr.exec()
        elif self.checkValue == '<':
            return self.leftExpr.exec() < self.rightExpr.exec()
        elif self.checkValue == '<=':
            return self.leftExpr.exec() <= self.rightExpr.exec()
