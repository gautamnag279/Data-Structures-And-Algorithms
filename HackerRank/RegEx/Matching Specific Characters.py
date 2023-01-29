Regex_Pattern = '^[1-3][0-2][xs0][30Aa][xsu][.,]$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
