import nltk as nltk
import re
from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA


class Lexer:

    def __init__(self):
        self.input = None
        self.allSymbols = ''

    def set_input(self, text):
        self.input = text

    def lexer(self):
        # defining tokens
        operators = "(:=)"
        keywords = "if|then|else|end"
        symbols = ";"
        numbers = r'(\d+)'
        identifier = '[a-z]'
        tokens = []
        # tokenizing the input file

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
                self.allSymbols = self.allSymbols + 'i'
            elif token == "then":
                self.allSymbols = self.allSymbols + 't'
            elif token == "else":
                self.allSymbols = self.allSymbols + 'e'
            elif token == 'end':
                self.allSymbols = self.allSymbols + 'n'
            elif token == ':=':
                self.allSymbols = self.allSymbols + 'o'
            elif token == ';':
                self.allSymbols = self.allSymbols + 's'
            elif token[0].isalpha():
                self.allSymbols = self.allSymbols + 'd'
            elif token.isdigit():
                self.allSymbols = self.allSymbols + 'z'
            else:
                self.allSymbols = self.allSymbols + 'x'  # not a valid lexeme

        return self.allSymbols

    def draw_dfa(self):

        dfa = VisualDFA(
            states={"start", "if", "then", "end", "stuck", "else", "condition", "identifier", "operator", "calculate",
                    "symbol"},  # id=y operator=o symbol=s
            input_symbols={"i", "t", "e", "n", "z", "o", "d", "s"},
            transitions={
                "start": {"i": "if", "t": "stuck", "e": "stuck", "n": "stuck", "z": "stuck", "o": "stuck", "d": "stuck",
                          "s": "stuck"},  # start
                "if": {"i": "stuck", "t": "stuck", "e": "stuck", "n": "stuck", "z": "condition", "o": "stuck",
                       "d": "stuck",
                       "s": "stuck"},  # if
                "then": {"i": "if", "t": "stuck", "e": "stuck", "n": "stuck", "z": "stuck", "o": "stuck",
                         "d": "identifier",
                         "s": "stuck"},  # then
                "else": {"i": "if", "t": "stuck", "e": "stuck", "n": "end", "z": "stuck", "o": "stuck",
                         "d": "identifier",
                         "s": "stuck"},  # else
                "end": {"i": "if", "t": "stuck", "e": "else", "n": "end", "z": "stuck", "o": "stuck", "d": "stuck",
                        "s": "stuck"},  # end
                "stuck": {"i": "stuck", "t": "stuck", "e": "stuck", "n": "stuck", "z": "stuck", "o": "stuck",
                          "d": "stuck",
                          "s": "stuck"},  # stuck
                "condition": {"i": "stuck", "t": "then", "z": "condition", "e": "stuck", "n": "stuck", "o": "stuck",
                              "d": "stuck", "s": "stuck"},  # number condition
                "identifier": {"i": "stuck", "t": "stuck", "e": "stuck", "n": "stuck", "z": "stuck", "d": "stuck",
                               "o": "operator", "s": "stuck"},  # cant make id = is for now
                "operator": {"i": "stuck", "t": "stuck", "e": "stuck", "n": "stuck", "z": "calculate", "d": "calculate",
                             "o": "stuck", "s": "stuck"},
                "calculate": {"i": "stuck", "t": "stuck", "e": "stuck", "n": "stuck", "z": "calculate", "d": "stuck",
                              "o": "stuck", "s": "symbol"},
                "symbol": {"i": "stuck", "t": "stuck", "e": "else", "n": "end", "z": "stuck", "d": "identifier",
                           "o": "stuck",
                           "s": "stuck"}
            },
            initial_state="start",
            final_states={"end"},
        )

        '''minimizedDFA = DFA.minify(dfa)'''

        dfa.show_diagram(self.allSymbols, view=True)

        '''print(allSymbols)'''


l = Lexer()
