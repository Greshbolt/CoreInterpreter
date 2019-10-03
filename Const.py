from Tokenizer import TokList
from Digit import Digit
class Const:
    def __init__(self):
        self.digit = None
        self.const = None
        self.name = ''
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
    def print(self):
        print(self.name, end='')
    def exec(self):
        return int(self.name)