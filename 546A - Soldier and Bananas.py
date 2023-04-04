k,n,w = map(int, input().split())

cost = 0
for i in range(1,w+1):
    cost += i*k

res = cost - n
if res < 0:
    print(0)
else:
    print(res)
