import nltk as nltk
import re
import ParsingTable as table
import ParserLexer as lex

global allSymbols
allSymbols = lex.lexer()
print(allSymbols)
global cursor
cursor = 0

global stack
stack=[0]





def shift(stack,allSymbols,x,cursor):

    stack.append(allSymbols[cursor])
    stack.append(x)
    cursor=cursor+1

    parse(stack,allSymbols)




def reduce(stack,rule):
    if(rule == 1):

        for i in reversed(stack):
            if(i>0 and stack[i]=="statement" and stack[i-1]=="stmt-seq" ):
                del stack[i]
                del stack[i-1]
                stack.append("stmt-seq")
                return
        notAccepted()

    elif (rule == 2):

        for i in reversed(stack):
            if (stack[i] == "statement"):
                del stack[i]
                stack.append("stmt-seq")
                return
        notAccepted()

    elif (rule == 3):

        for i in reversed(stack):
            if (stack[i] == "if-stmt"):
                del stack[i]
                stack.append("statement")
                return
        notAccepted()

    elif(rule == 4):

        for i in reversed(stack):
            if (stack[i] == "assign-stmt"):
                del stack[i]
                stack.append("statement")
                return
        notAccepted()

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
        notAccepted()


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
        notAccepted()

    elif (rule == 7):

        for i in reversed(stack):
            if (stack[i] == "identifier"):
                del stack[i]
                stack.append("factor")
                return
        notAccepted()

    elif (rule == 8):

        for i in reversed(stack):
            if (stack[i] == "number"):
                del stack[i]
                stack.append("factor")
                return
        notAccepted()

def notAccepted():
    print("String not accepted")

def action(stack,allSymbols,x,cursor):
    if (x[0] == 's'):  # if shift function
        shift(stack, allSymbols, int(x[1],10),cursor)
        print(stack)

    elif (x[0] == 'r'):  # if reduce function
        rule = int(x[1], 10)
        reduce(stack, allSymbols, rule)
        print(stack)


def parse(stack,allSymbols):
    inputToken = allSymbols[cursor]
    top = stack[len(stack)-1] #stores the top of stack
    if(isinstance(top,int)):  #checks if top of stack is integer

        if(inputToken=="if"): #if the input equals if
            x=table.If[top]   #retrieves the parsing table action in string
            action(stack, allSymbols, x,cursor)
            print(stack)

        elif(inputToken=="number"):
            x = table.number[top]
            action(stack, allSymbols, x,cursor)

        elif (inputToken == ":="):
            x = table.equal[top]
            action(stack, allSymbols, x,cursor)
        elif (inputToken == "identifier"):
            x = table.id[top]
            action(stack, allSymbols, x,cursor)
        elif (inputToken == "then"):
            x = table.then[top]
            action(stack, allSymbols, x,cursor)
        elif (inputToken == "end"):
            x = table.end[top]
            action(stack, allSymbols, x,cursor)
        elif (inputToken == ";"):
            x = table.semicolon[top]
            action(stack, allSymbols, x,cursor)
        elif (inputToken == "$"):
            x = table.dollar[top]
            action(stack, allSymbols, x,cursor)

    else:
        if (inputToken == "stmt-seq"):
          x=table.stmtseq[top-1]
          stack.append(x[1])
        elif (inputToken == "statement"):
            x = table.statement[top-1]
            stack.append(x[1])
        elif (inputToken == "if-stmt"):
            x = table.ifstmt[top-1]
            stack.append(x[1])
        elif (inputToken == "assign-stmt"):
            x = table.assignstmt[top-1]
            stack.append(x[1])
        elif (inputToken == "factor"):
            x = table.factor[top-1]
            stack.append(x[1])

parse(stack,allSymbols)
print(stack)