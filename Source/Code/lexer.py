import nltk as nltk
import re


def lexer():
    input_code = open("/Users/karim/Desktop/Compiler-Spring-2022/Source/Code/input",
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
