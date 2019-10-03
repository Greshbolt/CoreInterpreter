from program import Program
from Tokenizer import TokList
TokList.getFiles('t1.code','t1.data')
print(TokList.currentToken())
print(TokList.idDict)
print(TokList.tokenList)
