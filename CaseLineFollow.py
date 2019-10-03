from Tokenizer import TokList
import CaseLine
class CaseLineFollow:
    def __init__(self):
        self.caseLine = None
    def parse(self):
        if not TokList.checkTok('BAR'):
            return
        TokList.match('BAR', 'case line follow')
        self.caseLine = CaseLine.CaseLine()
        self.caseLine.parse()
    def print(self):
        if self.caseLine is not None:
            print('\n| ')
            self.caseLine.print()
    def exec(self, caseId):
        if self.caseLine is not None:
            return self.caseLine.exec(caseId)
        return False