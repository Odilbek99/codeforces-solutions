n = int(input())
line = list(map(int,input().split()))

c = 1
max_ = 1
for i in range(len(line)-1):
    if max_ == n:
        print(n)
        break
    elif line[i] <= line[i+1]:
        # print(line[i],line[i+1])
        c+=1
        max_ = max(c,max_)
    else:
        c=1

print(max_)
