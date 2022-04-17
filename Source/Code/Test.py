import nltk as nltk
import re


input_string = "if 1 then x := 5 ; y := 5 ; end"

#reg=re.compile(r'if\s\d\sthen(\s[a-z]\s:=\s\d\s;)+\send')#original

reg = re.compile(r'if\s\d\sthen(\s[a-z]\s:=\s\d\s;)+\send')
matches =reg.finditer(input_string)

for match in matches:
    print(match)
