a = input()

print(any(c.isalnum()for c in a))
print(any(c.isalpha() for c in a))
print(any(c.isdigit() for c in a))
print(any(c.islower() for c in a))
print(any(c.isupper()for c in a))
