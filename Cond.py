from Tokenizer import TokList
from Cmpr import Cmpr
class Cond:
    def __init__(self):
        self.cmpr = None
        self.cond = None
        self.notStr = None
    def parse(self):
        if TokList.checkTok('NOT'):
            self.notStr = '!'
            TokList.nextToken()
            TokList.match('LEFTPARAN', 'cond')
            self.cond = Cond()
            self.cond.parse()
            TokList.match('RIGHTPARAN', 'cond')
            return
        self.cmpr = Cmpr()
        self.cmpr.parse()
        if TokList.checkTok('OR'):
            TokList.nextToken()
            self.cond = Cond()
            self.cond.parse()
    def print(self):
        if self.notStr is not None:
            print(self.notStr+'(', end='')
            self.cond.print()
            print(')', end='')
        elif self.cmpr is not None and self.cond is not None:
            self.cmpr.print()
            self.cond.print()
        else:
            self.cmpr.print()
    def exec(self):
        if self.notStr is not None:
            return not self.cond.exec()
        elif self.cmpr is not None and self.cond is not None:
            return self.cmpr.exec() or self.cond.exec()
        else:
            return self.cmpr.exec()