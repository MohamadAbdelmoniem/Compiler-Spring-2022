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





def shift(stack,allSymbols,x):
    global cursor
    stack.append(allSymbols[cursor])
    stack.append(x)
    cursor=cursor+1
    print("cursor is " + str(cursor))




def reduce(stack,rule):
    i=len(stack)-1
    if(rule == 1):

        while i>=0:
            if(i>0 and stack[i-1]=="statement" and stack[i-3]=="stmt-seq" ):
                del stack[i]
                del stack[i-1]
                del stack[i - 2]
                del stack[i - 3]
                stack.append("stmt-seq")
                y = table.stmtseq[stack[len(stack) - 2]]
                stack.append(y)
                return
            i-=1
        notAccepted()

    elif (rule == 2):

        while i>=0:
            if (stack[i-1] == "statement"):
                del stack[i]
                del stack[i - 1]
                stack.append("stmt-seq")
                y = table.stmtseq[stack[len(stack) - 2]]
                stack.append(y)
                return
            i -= 1
        notAccepted()

    elif (rule == 3):

        while i>=0:
            if (stack[i-1] == "if-stmt"):
                del stack[i]
                del stack[i - 1]
                stack.append("statement")
                y = table.statement[stack[len(stack) - 2]]
                stack.append(y)
                return
            i -= 1
        notAccepted()

    elif(rule == 4):

        while i>=0:
            if (stack[i-1] == "assign-stmt"):
                del stack[i]
                del stack[i - 1]
                stack.append("statement")
                y = table.statement[stack[len(stack) - 2]]
                stack.append(y)
                return
            i -= 1
        notAccepted()

    elif (rule == 5):

        while i>=0:
            if (i>8 and stack[i-1] == "end" and stack[i-3]=="stmt-seq" and stack[i-5]=="then"
                    and stack[i-7]=="number" and stack[i-9]=="if"):

                del stack[i]
                del stack[i-1]
                del stack[i-2]
                del stack[i-3]
                del stack[i-4]
                del stack[i - 5]
                del stack[i - 6]
                del stack[i - 7]
                del stack[i - 8]
                del stack[i - 9]
                stack.append("if-stmt")
                y = table.ifstmt[stack[len(stack) - 2]]
                stack.append(y)
                return
            i -= 1
        notAccepted()


    elif (rule == 6):

        while i>=0:
            if (i>6 and stack[i-1] == ";" and stack[i-3]=="factor" and stack[i-5]==":="
                    and stack[i-7]=="identifier"):
                del stack[i]
                del stack[i - 1]
                del stack[i - 2]
                del stack[i - 3]
                del stack[i - 4]
                del stack[i - 5]
                del stack[i - 6]
                del stack[i - 7]
                stack.append("assign-stmt")
                y = table.assignstmt[stack[len(stack) - 2]]
                stack.append(y)
                return
            i -= 1
        notAccepted()

    elif (rule == 7):

        while i>=0:
            if (stack[i-1] == "identifier"):
                del stack[i]
                del stack[i-1]
                stack.append("factor")
                y=table.factor[stack[len(stack)-2]]
                stack.append(y)
                return
            i -= 1
        notAccepted()

    elif (rule == 8):

        while i>=0:
            if (stack[i-1] == "number"):
                del stack[i]
                del stack[i-1]
                stack.append("factor")
                y = table.factor[stack[len(stack) - 2]]
                stack.append(y)
                return
            i -= 1
        notAccepted()

def notAccepted():
    print("String not accepted")

def action(stack,allSymbols,x):
    if (x[0] == 's'):  # if shift function
        split = re.split('(\d+)', x)
        x = split[1]
        x=int(x,10)
        print("the int value is "+ str(x))
        shift(stack, allSymbols, x)
        print(stack)
        parse(stack,allSymbols)

    elif (x[0] == 'r'):  # if reduce function
        split = re.split('(\d+)', x)
        x = split[1]
        rule = int(x, 10)
        reduce(stack, rule)
        print(stack)
        parse(stack,allSymbols)
    elif(x=="accept"):
        stack.append("$")
        print(stack)
        print("String is accepted")
        print("Congratulations!")



def parse(stack,allSymbols):
    global cursor
    inputToken = allSymbols[cursor]
    print(inputToken)
    top = stack[len(stack)-1]
    print("top equals " + str(top))#stores the top of stack
    if(isinstance(top,int)):  #checks if top of stack is integer
        print("iteration")
        if(inputToken=="if"): #if the input equals if
            x=table.If[top]   #retrieves the parsing table action in string
            action(stack, allSymbols, x)


        elif(inputToken=="number"):
            x = table.number[top]
            print("number top is " + str(x))
            action(stack, allSymbols, x)

        elif (inputToken == ":="):
            x = table.equal[top]
            action(stack, allSymbols, x)
        elif (inputToken == "identifier"):
            x = table.id[top]
            action(stack, allSymbols, x)
        elif (inputToken == "then"):
            x = table.then[top]
            action(stack, allSymbols, x)
        elif (inputToken == "end"):
            x = table.end[top]
            action(stack, allSymbols, x)
        elif (inputToken == ";"):
            x = table.semicolon[top]
            action(stack, allSymbols, x)
        elif (inputToken == "$"):
            x = table.dollar[top]
            action(stack, allSymbols, x)

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

