import nltk as nltk
import re

from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA


def lexer():
    input_code = open("D:\Ziad\Projects\Compiler-Spring-2022\Source\Code\input",#replace by path to input file
                      'r')  # open input file in read mode

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

    input_code.close()


lexer()



dfa = DFA(
    states={"start","if","then","else","end","stuck"},
    input_symbols={"if","then","else","end"},
    transitions={
        "start":{"if":"if","then": "stuck","else" :"stuck","end":"stuck"},
        "if": {"if":"stuck","then": "then","else" :"stuck","end":"stuck"},
        "then":{"if":"stuck","then":"stuck","else":"else","end":"stuck"},
        "else":{"if":"stuck","then":"stuck","else":"stuck","end":"end"},
        "end":{"if":"stuck","then":"stuck","else":"stuck","end":"end"},
        "stuck":{"if":"stuck","then":"stuck","else":"stuck","end":"stuck"}
    },
    initial_state="start",
    final_states={"end"},
)

dfa = VisualDFA(dfa)
dfa.show_diagram("if")