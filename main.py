import re
text = input()
match = re.findall(r"[0123456789]",text)

print(match)
