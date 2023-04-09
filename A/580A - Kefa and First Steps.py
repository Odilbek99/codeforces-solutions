n = int(input())
line = list(map(int,input().split()))

c = 1
max_ = 0
for i in range(len(line)-1):
    
    if line[i] <= line[i+1]:
        print(line[i],line[i+1])
        c+=1
    else:
        max_ = max(c,max_)
        c=1

print(max_)
