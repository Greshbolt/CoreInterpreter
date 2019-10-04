from Tokenizer import TokList
from Letter import Letter
from Digit import Digit
class Id:
    def __init__(self):
        self.letter = None
        self.id = None
        self.digit = None
        self.name = ''
    #Recursive parsing to determine what combination of letters and digits the id is made up of based on string passed in.
    #This builds the name for the id
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
    #Simple print
    def print(self):
        print(self.name, end='')
    #Used for determining value of the id
    def exec(self):
        return self.getValue()
    #Sets the value and checks if the variable was ever even initialized
    def setValue(self, val):
        if TokList.getIdValue(self.name) is None:
            print('ERROR: Value not initialized')
        TokList.setIdValue(self.name,val)
    #Gets value of the variable and checks to see if it was even initialized or even given a value
    def getValue(self):
        if TokList.getIdValue(self.name) == 'null' or TokList.getIdValue(self.name) is None:
            print('ERROR: Value undeclared')
            exit()
        return int(TokList.getIdValue(self.name))