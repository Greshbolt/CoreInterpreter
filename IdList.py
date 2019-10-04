from Tokenizer import TokList
from Id import Id
class IdList:
    def __init__(self):
        self.id = None
        self.id_list = None
    #Simple parsing to check for further ids
    def parse(self):
        self.id = Id()
        #Passing in name of id to the parse function
        self.id.parse(TokList.getIdOrConst())
        TokList.nextToken()
        if TokList.checkTok('COMMA'):
            TokList.match('COMMA', 'id list')
            self.id_list = IdList()
            self.id_list.parse()
    #Simple printing
    def print(self):
        self.id.print()
        if(self.id_list is not None):
            print(',', end='')
            self.id_list.print()
    def exec(self):
        pass
    #Used to set the values of all variables in an Id List, init determines whether it is initialization or not
    def setIdValues(self, init):
        if init == 1:
            if TokList.getIdValue(self.id.name) == 'null':
                print('ERROR: value ' + self.id.name + ' is already initialized')
                exit()
            #Initialized to 'null' as None is the previous assignment, 'null' is used later to check for initialization
            TokList.setIdValue(self.id.name, 'null')
            if self.id_list is not None:
                self.id_list.setIdValues(1)
        else:
            self.id.setValue(TokList.currentData())
            TokList.nextData()
            if self.id_list is not None:
                self.id_list.setIdValues(0)