n = int(input())
line = list(map(int,input().split()))
d = {}
for i in range(len(line)):
    d[i] = line[i]
d = sorted(d.items(), key=lambda kv: kv[1])
res = ""
for key in d:
    res += str(key[0]+1) + ' '
print(res)
