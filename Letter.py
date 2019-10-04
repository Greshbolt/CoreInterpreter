from Tokenizer import TokList
#This is a barebones class to represent single letters
class Letter:
    def __init__(self):
        self.let = ''
    def parse(self, letStr):
        self.let = letStr
    def print(self):
        pass
    def exec(self):
        pass