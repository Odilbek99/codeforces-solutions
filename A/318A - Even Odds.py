n,k = map(int,input().split())
res = None
if n%2 == 0:
    if k > n//2:
        res = n - (n-k)*2
    else:
        res = (n-1) - ((n//2) - k)*2
else:
    if k > n//2 + 1:
        res = (n-1) - (n-k)*2
    else:
        res = n - (n//2 + 1 - k)*2

print(res)   
