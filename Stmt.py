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
    #Similar to algorithm in class, checks for type of statement and assigns an altNo based on that, if none are recognized it reports an error
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
            #Used to briefly check for and EOF exception
            TokList.match('', 'statement')
    #Simple printing using the altNo
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
    #Simple execution based on altNo evaluation
    def exec(self):
        if self.altNo == 1:
            self.s1.exec()
        elif self.altNo == 2:
            self.s2.exec()
        elif self.altNo == 3:
            self.s3.exec()
        elif self.altNo == 4:
            self.s4.exec()
        elif self.altNo == 5:
            self.s5.exec()
        elif self.altNo == 6:
            self.s6.exec()
        