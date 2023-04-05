n,h = map(int, input().split())
heights = list(map(int, input().split()))
c = 0
for i in heights:
    if i <= h:
        c += 1  
# print(n - c)
res = 2*(n - c) + c
print(res)
