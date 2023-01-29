Regex_Pattern = r'([a-z])(\w)(\s)([^\w])([0-9])([^0-9])([A-Z])([a-zA-Z])([aeiouAEIOU])(\S)\1\2\3\4\5\6\7\8\9\10'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
