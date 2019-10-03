from Tokenizer import TokList
from CaseLine import CaseLine
from Expr import Expr
from Id import Id
class Case:
    def __init__(self):
        self.case_line = None
        self.expr = None
        self.id = None
    def parse(self):
        TokList.match('CASE','case')
        self.id = Id()
        self.id.parse(TokList.getIdOrConst())
        TokList.nextToken()
        TokList.match('OF','case')
        self.case_line = CaseLine()
        self.case_line.parse()
        TokList.match('ELSE','case')
        self.expr = Expr()
        self.expr.parse()
        TokList.match('END','case')
        TokList.match('SEMICOLON','case')
    def print(self):
        print('case ')
        self.id.print()
        print(' of\n')
        self.case_line.print()
        print('else ')
        self.expr.print()
        print('end;')
    def exec(self):
        if not (self.case_line.exec(self.id)):
            self.id.setValue(self.expr.exec())