n = int(input())
line = list(map(int, input().split()))

mx = max(line)
mn = min(line)
mx_pos = None
mn_pos = None
for i in range(len(line)):
    if line[i] == mx:
        if mx_pos is None:
            mx_pos = i
        else:
            mx_pos = min(mx_pos,i)
line.insert(0,line[mx_pos])
line.pop(mx_pos+1)

for i in range(len(line)):

    if line[i] == mn:
        if mn_pos is None:
            mn_pos = i
        else:
            mn_pos = max(mn_pos,i)

# line.append(line[mn_pos])
# line.pop(mn_pos)
# print(line)

print(mx_pos+(n-(mn_pos+1)))
