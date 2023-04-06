y = int(input())

b = True
c = y
while b:
    c += 1
    if len(set(str(c))) == len(str(c)):
        print(c)
        break
