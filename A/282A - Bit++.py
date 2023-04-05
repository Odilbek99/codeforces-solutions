n = int(input())
res = 0
for i in range(n):
    stm = input()
    if '-' in stm:
        res -= 1
    else:
        res += 1
print(res)
