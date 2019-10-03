from Tokenizer import TokList
from Cond import Cond
import StmtSeq
class If:
    def __init__(self):
        self.cond = None
        self.stmt_seq_then = None
        self.stmt_seq_else = None
    def parse(self):
        TokList.match('IF', 'if')
        self.cond = Cond()
        self.cond.parse()
        TokList.match('THEN', 'if')
        self.stmt_seq_then = StmtSeq.StmtSeq()
        self.stmt_seq_then.parse()
        if TokList.checkTok('ELSE'):
            TokList.nextToken()
            self.stmt_seq_else = StmtSeq.StmtSeq()
            self.stmt_seq_else.parse()
        TokList.match('ENDIF', 'if')
        TokList.match('SEMICOLON', 'if')
    def print(self):
        TokList.printIndent()
        print('if ', end='')
        self.cond.print()
        print(' then')
        TokList.increaseIndent()
        self.stmt_seq_then.print()
        if self.stmt_seq_else is not None:
            TokList.decreaseIndent()
            TokList.printIndent()
            print('else')
            TokList.increaseIndent()
            self.stmt_seq_else.print()
        TokList.decreaseIndent()
        TokList.printIndent()
        print('endif;')
    def exec(self):
        if self.cond.exec():
            self.stmt_seq_then.exec()
        elif self.stmt_seq_else is not None:
            self.stmt_seq_else.exec()