from Tokenizer import TokList
from Assign import Assign
from If import If
from Loop import Loop
from In import In
from Out import Out
from Case import Case
class Stmt:
    def __init__(self):
        self.altNo = 0
        self.s1 = None
        self.s2 = None
        self.s3 = None
        self.s4 = None
        self.s5 = None
        self.s6 = None
    def parse(self):
        if TokList.checkTok('ID'):
            self.altNo = 1
            self.s1 = Assign()
            self.s1.parse()
        elif TokList.checkTok('IF'):
            self.altNo = 2
            self.s2 = If()
            self.s2.parse()
        elif TokList.checkTok('WHILE'):
            self.altNo = 3
            self.s3 = Loop()
            self.s3.parse()
        elif TokList.checkTok('INPUT'):
            self.altNo = 4
            self.s4 = In()
            self.s4.parse()
        elif TokList.checkTok('OUTPUT'):
            self.altNo = 5
            self.s5 = Out()
            self.s5.parse()
        elif TokList.checkTok('CASE'):
            self.altNo = 6
            self.s6 = Case()
            self.s6.parse()
        else:
            print('ERROR: Syntax error')
            exit()
        
    def print(self):
        if self.altNo == 1:
            self.s1.print()
        elif self.altNo == 2:
            self.s2.print()
        elif self.altNo == 3:
            self.s3.print()
        elif self.altNo == 4:
            self.s4.print()
        elif self.altNo == 5:
            self.s5.print()
        elif self.altNo == 6:
            self.s6.print()
    def exec(self):
        pass
        