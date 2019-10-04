from Tokenizer import TokList
from Digit import Digit
class Const:
    def __init__(self):
        self.digit = None
        self.const = None
        self.name = ''
    #Simple recursive parsing to build what value the const has, based on the string passed in
    def parse(self, constStr):
        length = len(constStr)
        if length <= 1:
            self.digit = Digit()
            self.digit.parse(constStr)
            self.name = self.digit.dig
        else:
            self.const = Const()
            self.const.parse(constStr[0:length-1])
            self.digit = Digit()
            self.digit.parse(constStr[length-1])
            self.name = self.const.name + self.digit.dig
    #Simple print
    def print(self):
        print(int(self.name), end='')
    #Simple execution that returns the value of the const
    def exec(self):
        return int(self.name)