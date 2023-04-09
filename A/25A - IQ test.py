n = int(input())
line = list(map(int,input().split()))
odd = 0
even = 0
for i in range(len(line)):
    if line[i] % 2 == 0:
        even += 1

    else:
        odd += 1
    
    if even >= 2:
        break
    if odd >= 2:
        break
# print(odd)
# # print(even)
if odd > even:
    for i in range(len(line)):
        if line[i]%2 == 0:
            print(i+1)
        else:
            continue
else:
    for i in range(len(line)):
        if line[i]%2 != 0:
            print(i+1)



