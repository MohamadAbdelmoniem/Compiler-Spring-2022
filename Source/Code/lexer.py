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
        elif token == ':=':
            allSymbols = allSymbols + 'o'
        elif token == ';':
            allSymbols = allSymbols + 's'
        elif token[0].isalpha():
            allSymbols = allSymbols + 'd'
        elif token.isdigit():
            allSymbols = allSymbols + 'z'
        else:
            allSymbols = allSymbols + 'x' #not a valid lexeme
    input_code.close()


lexer()



dfa2 = VisualDFA(
    states={"start","if","then","end","stuck","else","condition","identifier", "operator","calculate","symbol"},#id=y operator=o
    input_symbols={"i","t","e","n","z","o","d","s"},
    transitions={
        "start":{"i":"if","t": "stuck","e" :"stuck","n":"stuck","z":"stuck","o":"stuck","d":"stuck","s":"stuck"}, #start
        "if":{"i":"stuck","t": "stuck","e" :"stuck","n":"stuck","z":"condition","o":"stuck","d":"stuck","s":"stuck"},#if
        "then":{"i":"stuck","t":"stuck","e":"stuck","n":"stuck","z":"stuck","o":"stuck","d":"identifier","s":"stuck"},#then
        "else":{"i":"if","t":"stuck","e":"stuck","n":"end","z":"stuck","o":"stuck","d":"identifier","s":"stuck"},#else
        "end":{"i":"stuck","t":"stuck","e":"stuck","n":"end","z":"stuck","o":"stuck","d":"stuck","s":"stuck"},#end
        "stuck":{"i":"stuck","t":"stuck","e":"stuck","n":"stuck","z":"stuck","o":"stuck","d":"stuck","s":"stuck"},#stuck
        "condition":{"i":"stuck","t":"then","z":"condition","e":"stuck","n":"stuck","o":"stuck","d":"stuck","s":"stuck"},#number condition
        "identifier" : {"i":"stuck","t":"stuck","e":"stuck","n":"stuck","z":"stuck","d":"stuck","o":"operator","s":"stuck"},#cant make id = is for now
        "operator" :  {"i":"stuck","t":"stuck","e":"stuck","n":"stuck","z":"calculate","d":"calculate","o":"stuck","s":"stuck"},
        "calculate":{"i":"stuck","t":"stuck","e":"stuck","n":"stuck","z":"calculate","d":"stuck","o":"stuck","s":"symbol"},
        "symbol" : {"i":"stuck","t":"stuck","e":"else","n":"end","z":"stuck","d":"identifier","o":"stuck","s":"stuck"}
    },
    initial_state="start",
    final_states={"end"},
)



dfa2.show_diagram(allSymbols,view=True)
print(allSymbols)