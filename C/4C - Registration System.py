n = int(input())
d = {}
for i in range(n):
    s = input()
    if d.get(s) is None:
        d[s] = 0
        print('OK')
    else:
        d[s] += 1
        print(s+str(d[s]))

    
    
