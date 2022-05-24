import nltk as nltk
import re
import ParsingTable as table

stack=[0]


def lexer():
    input_code = open("D:\Ziad\Projects\Compiler-Spring-2022\Source\Code\input",  # replace by path to input file
                      'r')  # open input file in read mode
    allSymbols = ""
    # defining tokens
    operators = "(:=)"
    keywords = "if|then|else|end"
    symbols = ";"
    numbers = r'(\d+)'
    identifier = '[a-z]'
    tokens = []
    # tokenizing the input file
    lines = input_code.readlines()
    print(lines)
    for line in lines:
        tokens.extend(nltk.wordpunct_tokenize(line))
    print(tokens)
    # printing tokens
    for token in tokens:
        if re.findall(operators, token):
            print(token, "is an operator")
        elif re.findall(numbers, token):
            print(token, "is a number")
        elif re.findall(keywords, token):
            print(token, "is a keyword")
        elif re.findall(symbols, token):
            print(token, "is a symbol")
        elif re.findall(identifier, token):
            print(token, "is an identifier")
    for token in tokens:  # gives the tokens a code symbol
        if token == "if":
            allSymbols = allSymbols + 'if '
        elif token == "then":
            allSymbols = allSymbols + 'then '
        elif token == "else":
            allSymbols = allSymbols + 'e'
        elif token == 'end':
            allSymbols = allSymbols + 'end '
        elif token == ':=':
            allSymbols = allSymbols + ':= '
        elif token == ';':
            allSymbols = allSymbols + '; '
        elif token[0].isalpha():
            allSymbols = allSymbols + 'identifier '
        elif token.isdigit():
            allSymbols = allSymbols + 'number '
        else:
            allSymbols = allSymbols + 'x'  # not a valid lexeme

    input_code.close()
    return allSymbols + "$"


allSymbols = lexer()
print(allSymbols)

cursor = 0

def parse(stack,allsymbols):
    inputToken=allSymbols[cursor]
    top= stack[len(stack)-1]
    if(isinstance(top,int)):  #checks if top of stack is integer

        if(inputToken=="if"): #if the input equals if
            x=table.If[top]   #retrieves the parsing table action in string

            if(x[0]=='s'):    #if shift function
                shift(stack,allsymbols,cursor)

            elif(x[0]=='r'):  #if reduce function
                rule = int(x[1],10)
                reduce(stack,allsymbols,rule)






def shift(stack,allsymbols,cursor):
    stack.append(allsymbols[cursor])
    cursor=cursor+1

def reduce(stack,allsymbols,rule):
    if(rule == 1):

        for i in reversed(stack):
            if(i>0 and stack[i]=="statement" and stack[i-1]=="stmt-seq" ):
                del stack[i]
                del stack[i-1]
                stack.append("stmt-seq")
                return

    elif (rule == 2):

        for i in reversed(stack):
            if (stack[i] == "statement"):
                del stack[i]
                stack.append("stmt-seq")
                return

    elif (rule == 3):

        for i in reversed(stack):
            if (stack[i] == "if-stmt"):
                del stack[i]
                stack.append("statement")
                return

    elif(rule == 4):

        for i in reversed(stack):
            if (stack[i] == "assign-stmt"):
                del stack[i]
                stack.append("statement")
                return

    elif (rule == 5):

        for i in reversed(stack):
            if (i>3 and stack[i] == "end" and stack[i-1]=="stmt-seq" and stack[i-2]=="then"
                    and stack[i-3]=="number" and stack[i-4]=="if"):

                del stack[i]
                del stack[i-1]
                del stack[i-2]
                del stack[i-3]
                del stack[i-4]
                stack.append("if-stmt")
                return


    elif (rule == 6):

        for i in reversed(stack):
            if (i>2 and stack[i] == ";" and stack[i-1]=="factor" and stack[i-2]==":="
                    and stack[i-3]=="identifier"):
                del stack[i]
                del stack[i - 1]
                del stack[i - 2]
                del stack[i - 3]
                stack.append("assign-stmt")
                return

    elif (rule == 7):

        for i in reversed(stack):
            if (stack[i] == "identifier"):
                del stack[i]
                stack.append("factor")
                return

    if (rule == 8):

        for i in reversed(stack):
            if (stack[i] == "number"):
                del stack[i]
                stack.append("factor")
                return