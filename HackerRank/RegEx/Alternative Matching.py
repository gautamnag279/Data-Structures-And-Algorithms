Regex_Pattern = r'^(Mr|Mrs|Mr|Dr|Er)\.[a-zA-Z]+$'	# Do not delete

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
