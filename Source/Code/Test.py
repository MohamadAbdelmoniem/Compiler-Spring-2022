import nltk as nltk
import re
import tokens as tk

input_string = "if 1 then x := 5 ; y := 5 ; end"

reg=re.compile(r'if\s\d\sthen(\s[a-z]\s:=\s\d\s;)+\send')

matches=reg.finditer(input_string)
for match in matches:
    print(match)
#x=re.search("^if\d+then",input_string)
#print(x)


'''tokens = nltk.wordpunct_tokenize(input_string)
print("tokens are:",tokens)
for token in tokens:
    if token in tk.operators.keys():
        print(token,"is an",tk.operators.get(token))

    if token in tk.symbols.keys():
        print(token,"is a",tk.symbols.get(token))

    if token in tk.keywords.keys():
        print(token,"is a keyword",tk.keywords.get(token))'''

