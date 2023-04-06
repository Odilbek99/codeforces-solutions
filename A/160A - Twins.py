n = int(input())
line = list(map(int,input().split()))

line_sum = sum(line)
line_sorted = sorted(line, reverse=True)
min_coin = line_sum//2

sum_ = 0
c = 0
for i in line_sorted:
    sum_ += i
    c+=1
    if sum_ > min_coin:
        break

    
print(c)