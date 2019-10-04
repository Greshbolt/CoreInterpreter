from Tokenizer import TokList
from Factor import Factor
class Term:
    def __init__(self):
        self.factor = None
        self.term = None
    #Simple parse statement that checks for multiplication
    def parse(self):
        self.factor = Factor()
        self.factor.parse()
        if TokList.checkTok('MULT'):
            TokList.nextToken()
            self.term = Term()
            self.term.parse()
    #Simple print statement
    def print(self):
        self.factor.print()
        if self.term is not None:
            print('*', end='')
            self.term.print()
    #Simple execution statement that returns a value based on parsing
    def exec(self):
        if self.term is not None:
            return self.factor.exec() * self.term.exec()
        return self.factor.exec()