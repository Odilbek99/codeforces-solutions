k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

dragons_list = [None]*d

for i in range(1,d+1):
    if i%k == 0 or i%l == 0 or i%m == 0 or i%n == 0:
        dragons_list[i-1] = 1
print(d-dragons_list.count(None))

