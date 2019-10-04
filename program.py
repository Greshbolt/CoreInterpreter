from Tokenizer import TokList
from DeclSeq import DeclSeq
from StmtSeq import StmtSeq
class Program:
    def __init__(self):
        self.decl_seq = None
        self.stmt_seq = None
    #Simple parsing with an error checking in the end
    def parse(self):
        TokList.match("PROGRAM", "program")
        self.decl_seq = DeclSeq()
        self.decl_seq.parse()
        TokList.match("BEGIN", "program")
        self.stmt_seq = StmtSeq()
        self.stmt_seq.parse()
        TokList.match("END", "program")
        #Checks for code after end of program
        if not TokList.checkTok('EOF'):
            print("ERROR: Improper code after end of program")
    #Prints program
    def print(self):
        print("program")
        TokList.increaseIndent()
        self.decl_seq.print()
        TokList.decreaseIndent()
        print("begin")
        TokList.increaseIndent()
        self.stmt_seq.print()
        TokList.decreaseIndent()
        print("end")
    #Executes program
    def exec(self):
        self.decl_seq.exec()
        self.stmt_seq.exec()


