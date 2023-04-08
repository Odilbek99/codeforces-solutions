n = int(input())
c = 1
res = ''
for i in range(n):
    mag = input()
    if res == '':
        res += mag
    elif res[1] == mag[0]:
        c += 1
        res = mag

print(c)