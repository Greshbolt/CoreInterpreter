from program import Program
from Tokenizer import TokList
import sys
TokList.getFiles(sys.argv[1],sys.argv[2])
p = Program()
p.parse()
p.print()
p.exec()

