import nltk as nltk
import re
def lexer():
    input_code = open("D:\Ziad\Projects\Compiler-Spring-2022\Source\Code\input",  # replace by path to input file
                      'r')  # open input file in read mode
    language = []
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
            language.append('if')

        elif token == "then":
            language.append('then')

        elif token == "else":
            language.append('e')

        elif token == 'end':
            language.append('end')

        elif token == ':=':
            language.append(':=')

        elif token == ';':
            language.append(';')

        elif token[0].isalpha():
            language.append('identifier')

        elif token.isdigit():
            language.append('number')

        else:
            language.append('x')  # not a valid lexeme

    input_code.close()
    language.append('$')
    return language