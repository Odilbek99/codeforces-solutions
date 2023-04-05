str1 = list(map(int, input().split('+')))
str1.sort()
res = '+'.join(map(str, str1))
print(res)