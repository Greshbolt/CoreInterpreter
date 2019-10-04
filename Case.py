from Tokenizer import TokList
from CaseLine import CaseLine
from Expr import Expr
from Id import Id
#As this was done as a class homework the results here will be very similar.
class Case:
    def __init__(self):
        self.case_line = None
        self.expr = None
        self.id = None
    #Simple parse of the case statement
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
    #Printing with proper indentation manipulation and new line printings
    def print(self):
        TokList.printIndent()
        print('case ', end='')
        self.id.print()
        print(' of')
        TokList.increaseIndent()
        TokList.printIndent()
        self.case_line.print()
        #Necessary for new line printings
        print()
        TokList.printIndent()
        print('else ', end='')
        self.expr.print()
        print()
        TokList.decreaseIndent()
        TokList.printIndent()
        print('end;')
    #Recursive execution based on values in the case line.  Id value is passed in to all versions of case
    def exec(self):
        if not (self.case_line.exec(self.id)):
            self.id.setValue(self.expr.exec())