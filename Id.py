from Tokenizer import TokList
from Letter import Letter
from Digit import Digit
class Id:
    def __init__(self):
        self.letter = None
        self.id = None
        self.digit = None
        self.name = ''
    def parse(self, idStr):
        length = len(idStr)
        if length <= 1:
            self.letter = Letter()
            self.letter.parse(idStr)
            self.name = self.letter.let
        elif idStr[length-1].isalpha:
            self.letter = Letter()
            self.letter.parse(idStr[length-1])
            self.id = Id()
            self.id.parse(idStr[0:length-1])
            self.name = self.id.name+self.letter.let
        elif idStr[length-1].isnumeric():
            self.digit = Digit()
            self.digit.parse(idStr[length-1])
            self.id = Id()
            self.id.parse(idStr[0:length-1])
            self.name = self.id.name + self.digit.dig
    def print(self):
        print(self.name, end='')
    def exec(self):
        return self.getValue()
    def setValue(self, val):
        TokList.setIdValue(self.name,val)
    def getValue(self):
        if TokList.getIdValue(self.name) == 'null':
            print('ERROR: Value undeclared')
            exit()
        return int(TokList.getIdValue(self.name))