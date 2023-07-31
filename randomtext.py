import random

s = "shut up homie"
s = "".join( random.choice([k.upper(), k ]) for k in s )
print(s)
