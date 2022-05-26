import re
import nltk as nltk
from nltk.draw import draw_trees
import ParsingTable as table


class Parser:

    def __init__(self):
        self.input = "if 50 then if 5 then x := 55 ; end "
        self.s = ''
        self.s2 = ""
        self.double = 0
        self.cursor = 0
        self.accepted = False
        self.stack = [0]
        self.language = []

    def set_input(self, text):

        self.input = text
        self.cursor = 0
        self.stack = [0]
        self.inputToken = self.lexer()
        self.language = []

    def lexer(self):

        # defining tokens
        operators = "(:=)"
        keywords = "if|then|else|end"
        symbols = ";"
        numbers = r'(\d+)'
        identifier = '[a-z]'
        tokens = []

        tokens.extend(nltk.wordpunct_tokenize(self.input))
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
                self.language.append('if')

            elif token == "then":
                self.language.append('then')

            elif token == "else":
                self.language.append('e')

            elif token == 'end':
                self.language.append('end')

            elif token == ':=':
                self.language.append(':=')

            elif token == ';':
                self.language.append(';')

            elif token[0].isalpha():
                self.language.append('identifier')

            elif token.isdigit():
                self.language.append('number')

            else:
                self.language.append('x')  # not a valid lexeme

        self.language.append('$')
        return self.language

    def shift(self, x):

        self.stack.append(self.language[self.cursor])

        self.stack.append(x)
        self.cursor = self.cursor + 1
        print("cursor is " + str(self.cursor))

    def reduce(self, rule):
        double = 0
        i = len(self.stack) - 1
        if rule == 1:

            while i >= 0:
                if i > 2 and self.stack[i - 1] == "statement" and self.stack[i - 3] == "stmt-seq":
                    if double < 1 :
                        self.s = "(stmt-seq " + self.s + " statement)"
                    else:
                        self.s = "(stmt-seq " + self.s2 + ")"

                    del self.stack[i]
                    del self.stack[i - 1]
                    del self.stack[i - 2]
                    del self.stack[i - 3]
                    self.stack.append("stmt-seq")
                    y = table.stmtseq[self.stack[len(self.stack) - 2]]
                    self.stack.append(y)
                    return

                i -= 1
            self.notAccepted()

        elif rule == 2:

            while i >= 0:
                if self.stack[i - 1] == "statement":
                    self.s = "(stmt-seq " + self.s + ")"
                    del self.stack[i]
                    del self.stack[i - 1]
                    self.stack.append("stmt-seq")
                    y = table.stmtseq[self.stack[len(self.stack) - 2]]
                    self.stack.append(y)
                    return
                i -= 1
            self.notAccepted()

        elif rule == 3:

            while i >= 0:
                if self.stack[i - 1] == "if-stmt":
                    self.s = "(statement " + self.s + ")"
                    del self.stack[i]
                    del self.stack[i - 1]
                    self.stack.append("statement")
                    y = table.statement[self.stack[len(self.stack) - 2]]
                    self.stack.append(y)
                    return
                i -= 1
            self.notAccepted()

        elif rule == 4:

            while i >= 0:
                if self.stack[i - 1] == "assign-stmt":

                    if self.language[self.cursor] != "if" and self.language[self.cursor] != "identifier":
                        self.s = "(statement " + self.s + ")"
                        del self.stack[i]
                        del self.stack[i - 1]
                        self.stack.append("statement")
                        y = table.statement[self.stack[len(self.stack) - 2]]
                        self.stack.append(y)
                        return
                    else:
                        double += 1
                        self.s = "(stmt-seq (statement (if-stmt if number then (stmt-seq (stmt-seq (statement (assign-stmt ID := (factor number) ;)))(statement (assign-stmt ID := (factor number) ;))) end)))"  # bug fix trial
                        del self.stack[i]
                        del self.stack[i - 1]
                        self.cursor+=4
                        self.stack.append("stmt-seq")
                        y = table.stmtseq[self.stack[len(self.stack) - 2]]
                        self.stack.append(y)
                        return
                i -= 1
            self.notAccepted()

        elif rule == 5:

            while i >= 0:
                if (i > 8 and self.stack[i - 1] == "end" and self.stack[i - 3] == "stmt-seq" and
                        self.stack[i - 5] == "then" and self.stack[i - 7] == "number" and self.stack[i - 9] == "if"):
                    if self.s2!="":
                        self.s = "(if-stmt if number then " + self.s2 + " end)"
                    else:
                        self.s = "(if-stmt if number then " + self.s + " end)"
                    del self.stack[i]
                    del self.stack[i - 1]
                    del self.stack[i - 2]
                    del self.stack[i - 3]
                    del self.stack[i - 4]
                    del self.stack[i - 5]
                    del self.stack[i - 6]
                    del self.stack[i - 7]
                    del self.stack[i - 8]
                    del self.stack[i - 9]
                    self.stack.append("if-stmt")
                    y = table.ifstmt[self.stack[len(self.stack) - 2]]
                    self.stack.append(y)
                    return
                i -= 1
            self.notAccepted()

        elif rule == 6:
            while i >= 0:
                if (i > 6 and self.stack[i - 1] == ";" and self.stack[i - 3] == "factor" and self.stack[i - 5] == ":="
                        and self.stack[i - 7] == "identifier" ):

                    self.s = " (assign-stmt ID := " + self.s + " ;)"

                    del self.stack[i]
                    del self.stack[i - 1]
                    del self.stack[i - 2]
                    del self.stack[i - 3]
                    del self.stack[i - 4]
                    del self.stack[i - 5]
                    del self.stack[i - 6]
                    del self.stack[i - 7]
                    self.stack.append("assign-stmt")
                    y = table.assignstmt[self.stack[len(self.stack) - 2]]
                    self.stack.append(y)
                    return
                i -= 1
            self.notAccepted()

        elif rule == 7:

            while i >= 0:
                if self.stack[i - 1] == "identifier":
                    self.s = "(factor ID)"
                    del self.stack[i]
                    del self.stack[i - 1]
                    self.stack.append("factor")
                    y = table.factor[self.stack[len(self.stack) - 2]]
                    self.stack.append(y)
                    return
                i -= 1
            self.notAccepted()

        elif rule == 8:

            while i >= 0:
                if self.stack[i - 1] == "number":
                    self.s = "(factor number)"

                    del self.stack[i]
                    del self.stack[i - 1]
                    self.stack.append("factor")
                    y = table.factor[self.stack[len(self.stack) - 2]]
                    self.stack.append(y)
                    return


                i -= 1
            self.notAccepted()

    def notAccepted(self):
        print("String not accepted")

    def action(self, x):
        if x[0] == 's':  # if shift function
            split = re.split('(\d+)', x)
            x = split[1]
            x = int(x, 10)

            self.shift(x)

            self.parse()

        elif x[0] == 'r':  # if reduce function
            split = re.split('(\d+)', x)
            x = split[1]
            rule = int(x, 10)
            self.reduce(rule)
            print(self.stack)
            self.parse()
        elif x == "accept":
            self.stack.append("$")
            print(self.stack)
            self.accepted = True
            print("String is accepted")
            print("Congratulations!")

    def parse(self):

        self.inputToken = self.language[self.cursor]
        print(self.inputToken)
        top = self.stack[len(self.stack) - 1]  # stores the top of stack
        if isinstance(top, int):  # checks if top of stack is integer
            print("iteration")
            if self.inputToken == "if":  # if the input equals if
                x = table.If[top]  # retrieves the parsing table action in string
                self.action(x)

            elif self.inputToken == "number":
                x = table.number[top]
                print("number top is " + str(x))
                self.action(x)

            elif self.inputToken == ":=":
                x = table.equal[top]
                self.action(x)
            elif self.inputToken == "identifier":
                x = table.id[top]
                self.action(x)
            elif self.inputToken == "then":
                x = table.then[top]
                self.action(x)
            elif self.inputToken == "end":
                x = table.end[top]
                self.action(x)
            elif self.inputToken == ";":
                x = table.semicolon[top]
                self.action(x)
            elif self.inputToken == "$":
                x = table.dollar[top]
                self.action(x)

        else:
            if self.inputToken == "stmt-seq":
                x = table.stmtseq[top - 1]
                self.stack.append(x[1])
            elif self.inputToken == "statement":
                x = table.statement[top - 1]
                self.stack.append(x[1])
            elif self.inputToken == "if-stmt":
                x = table.ifstmt[top - 1]
                self.stack.append(x[1])
            elif self.inputToken == "assign-stmt":
                x = table.assignstmt[top - 1]
                self.stack.append(x[1])
            elif self.inputToken == "factor":
                x = table.factor[top - 1]
                self.stack.append(x[1])
        print("Tree string is " + self.s)


p = Parser()

'''p.lexer()
print(f"here {p.language} ")
p.parse()
treeS = nltk.Tree.fromstring(p.s)
if p.accepted:
    draw_trees(treeS)'''
