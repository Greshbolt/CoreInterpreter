from Tokenizer import TokList
import CaseLine
class CaseLineFollow:
    def __init__(self):
        self.caseLine = None
    #parsing that determines if the case line continues.
    def parse(self):
        if not TokList.checkTok('BAR'):
            return
        TokList.match('BAR', 'case line follow')
        self.caseLine = CaseLine.CaseLine()
        self.caseLine.parse()
    #A print that executes only if a BAR is detected
    def print(self):
        if self.caseLine is not None:
            print()
            TokList.printIndent()
            print('|', end='')
            self.caseLine.print()
    #Executor that checks the caseline and returns false if it doesn't exist
    def exec(self, caseId):
        if self.caseLine is not None:
            return self.caseLine.exec(caseId)
        return False