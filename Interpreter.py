from program import Program
from Tokenizer import TokList
TokList.getFiles('bad2.code','bad5.data')
p = Program()
p.parse()
p.print()
p.exec()

