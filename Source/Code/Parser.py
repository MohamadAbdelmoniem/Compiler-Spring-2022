import nltk as nltk
import re


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
    return allSymbols


allSymbols = lexer()
print(allSymbols)

