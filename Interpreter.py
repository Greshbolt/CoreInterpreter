from program import Program
from Tokenizer import TokList
import sys
#Recieves the command line arguements for execution
TokList.getFiles(sys.argv[1],sys.argv[2])
#Declares the program object
p = Program()
#Parses, prints, and executes
p.parse()
p.print()
p.exec()

