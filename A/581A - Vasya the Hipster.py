a,b = map(int,input().split())

res = f'{min(a,b)} {int(abs(a-b)/2)}'
print(res)