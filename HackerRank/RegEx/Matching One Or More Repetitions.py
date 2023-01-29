Regex_Pattern = r'^[\d]{1,}[A-Z]{1,}[a-z]{1,}$'
#Regex_Pattern = r'^[\d]+[A-Z]+[a-z]+$' - this also works

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
