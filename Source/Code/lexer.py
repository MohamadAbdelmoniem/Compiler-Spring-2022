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
        if token == "then":
            allSymbols = allSymbols + 't'
        if token == "else":
            allSymbols = allSymbols + 'e'
        if token == 'end':
            allSymbols = allSymbols + 'n'
        if type(token) == int:
            allSymbols = allSymbols + 'z'
    input_code.close()


lexer()



dfa2 = VisualDFA(
    states={"q0","q1","q2","q4","q5","q3","q6"},
    input_symbols={"i","t","e","n","z"},
    transitions={
        "q0":{"i":"q1","t": "q5","e" :"q5","n":"q5","z":"q5"}, #start
        "q1":{"i":"q5","t": "q5","e" :"q5","n":"q5","z":"q6"},#if
        "q2":{"i":"q5","t":"q5","e":"q3","n":"q5","z":"q5"},#then
        "q3":{"i":"q5","t":"q5","e":"q5","n":"q4","z":"q5"},#else
        "q4":{"i":"q5","t":"q5","e":"q5","n":"q4","z":"q5"},#end
        "q5":{"i":"q5","t":"q5","e":"q5","n":"q5","z":"q5"},#stuck
        "q6":{"i":"q5","t":"q2","z":"q6","e":"q5","n":"q5"}#number
    },
    initial_state="q0",
    final_states={"q4"},
)



dfa2.show_diagram(allSymbols,view=True)
print(allSymbols)