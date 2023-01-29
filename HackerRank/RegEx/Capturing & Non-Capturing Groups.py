Regex_Pattern = r'(ok){3,}?'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

#QUANTIFIERS LOOK UP WEBSITE
https://docs.microsoft.com/en-us/dotnet/standard/base-types/quantifiers-in-regular-expressions?redirectedfrom=MSDN
