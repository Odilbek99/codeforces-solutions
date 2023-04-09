s = input()
if len(s) > 2:
    l = set(s[1:-1].split(', '))
    print(len(l))
else:
    print(0)