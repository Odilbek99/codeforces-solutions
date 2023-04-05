n = int(input())
d = {}
d['x'] = 0
d['y'] = 0
d['z'] = 0
for i in range(n):
    x,y,z = map(int, input().split())
    
    d['x'] += x
    d['y'] += y
    d['z'] += z

if list(d.values()).count(0) != 3:
    print('NO')
else:
    print('YES')
