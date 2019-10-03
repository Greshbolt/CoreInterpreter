from Tokenizer import TokList
from Id import Id
class IdList:
    def __init__(self):
        self.id = None
        self.id_list = None
    def parse(self):
        self.id = Id()
        self.id.parse(TokList.getIdOrConst())
        TokList.nextToken()
        if TokList.checkTok('COMMA'):
            TokList.match('COMMA', 'id list')
            self.id_list = IdList()
            self.id_list.parse()
    def print(self):
        self.id.print()
        if(self.id_list is not None):
            print(',', end='')
            self.id_list.print()
    def exec(self):
        pass
    def setIdValues(self):
        self.id.setValue(TokList.currentData())
        TokList.nextData()
        if self.id_list is not None:
            self.id_list.setIdValues()