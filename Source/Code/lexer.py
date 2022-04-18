import nltk as nltk
import re

from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA


def lexer():
    input_code = open("D:\Ziad\Projects\Compiler-Spring-2022\Source\Code\input",#replace by path to input file
                      'r')  # open input file in read mode
    global allSymbols
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
    for token in tokens: #gives the tokens a code symbol
        if token == "if":
            allSymbols = 'i'
        elif token == "then":
            allSymbols = allSymbols + 't'
        elif token == "else":
            allSymbols = allSymbols + 'e'
        elif token == 'end':
            allSymbols = allSymbols + 'n'
        elif token.isdigit():
            allSymbols = allSymbols + 'z'
        else:
            allSymbols = allSymbols + 'x' #not a valid lexeme
    input_code.close()


lexer()



dfa2 = VisualDFA(
    states={"start","if","then","end","stuck","else","integer","identifier", "keyword"},
    input_symbols={"i","t","e","n","z","y"},
    transitions={
        "start":{"i":"if","t": "stuck","e" :"stuck","n":"stuck","z":"stuck"}, #start
        "if":{"i":"stuck","t": "stuck","e" :"stuck","n":"stuck","z":"integer"},#if
        "then":{"i":"stuck","t":"stuck","e":"else","n":"stuck","z":"stuck"},#then
        "else":{"i":"stuck","t":"stuck","e":"stuck","n":"end","z":"stuck"},#else
        "end":{"i":"stuck","t":"stuck","e":"stuck","n":"end","z":"stuck"},#end
        "stuck":{"i":"stuck","t":"stuck","e":"stuck","n":"stuck","z":"stuck"},#stuck
        "integer":{"i":"stuck","t":"then","z":"integer","e":"stuck","n":"stuck"}#number condition

    },
    initial_state="start",
    final_states={"end"},
)



dfa2.show_diagram(allSymbols,view=True)
