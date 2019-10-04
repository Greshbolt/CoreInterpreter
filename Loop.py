from Tokenizer import TokList
from Cond import Cond
import StmtSeq
class Loop:
    def __init__(self):
        self.cond = None
        self.stmt_seq = None
    #Simple parsing to determine loop contents and conditional
    def parse(self):
        TokList.match('WHILE', 'loop')
        self.cond = Cond()
        self.cond.parse()
        TokList.match('BEGIN', 'loop')
        self.stmt_seq = StmtSeq.StmtSeq()
        self.stmt_seq.parse()
        TokList.match('ENDWHILE', 'loop')
        TokList.match('SEMICOLON', 'loop')
    #Simple printing with proper indentation manipulation
    def print(self):
        TokList.printIndent()
        print('while ', end='')
        self.cond.print()
        print(' begin')
        TokList.increaseIndent()
        self.stmt_seq.print()
        TokList.decreaseIndent()
        TokList.printIndent()
        print('endwhile;')
    #Executor that runs based on the condition given
    def exec(self):
        while self.cond.exec():
            self.stmt_seq.exec()