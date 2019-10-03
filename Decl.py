from Tokenizer import TokList
from IdList import IdList
class Decl:
    def __init__(self):
        self.id_list = None
    def parse(self):
        TokList.match('INT')
        self.id_list = IdList()