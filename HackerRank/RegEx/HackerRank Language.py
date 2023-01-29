import re

pattern = r'^[1-9]\d{4}\s(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$'

for _ in range(0, int(input())):
    s = input()
    if re.match(pattern , s):
        print("VALID")
    else:
        print("INVALID")
