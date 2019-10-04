# CoreInterpreter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                Jonathan Karkour
Files Submitting:
    (I created a file for each token in the core language so any files that
    share the parse, print, exec, will be represented with * after the first
    is described.)
    Assign.py - Manages the parse, print, and execute functions for the 
        Assign statement
    Case.py - *
    CaseLine.py - *
    CaseLineFollow.py - *
    Cmpr.py - *
    Cond.py - *
    Const.py - *
    ConstList.py - *
    Decl.py - *
    DeclSeq.py - *
    Digit.py - Used to represent single digits
    DOC.txt - Design description and scanner and parser interactions description
    Expr.py - *
    Factor.py - *
    Id.py - *
    IdList.py - *
    If.py - *
    In.py - *
    Interpreter.py - Takes in command line arguements, calls the Tokenizer,
        calls program, and parses, prints, and executes program
    Letter.py - Used to represent single letters
    Loop.py - *
    Out.py - *
    program.py - *
    README.txt - This file
    scanner.py - Used to access files given and create both a list of tokens and
        a list of integers provided in the data file
    Stmt.py - *
    StmtSeq.py - *
    Term.py - *
    Tokenizer.py - Is a globally accessed class which contains a dictionary of Ids,
        list of tokens, and list of data integers.  Contains functions to manipulate 
        each of these values as well as access them as well as indentation functionalities
Instructions for running:
    Make sure that all the files (including those provided in the command line) are in
    the same folder.  Once this is complete enter the following command:
                        python3 ./Interpreter.py {file.code} {file.data}
    Where both {file.code} and {file.data} are replaced by your respective .code and .data
    files.
Special features or comments:
    None