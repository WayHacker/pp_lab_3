import re
text = input()
match = re.findall(r"[0123456789]",text)
#comment for commit, nice :D
print(match)
