import string
n = int(input())
s = input().lower()

alphabet = string.ascii_lowercase
res = ''
for i in s:
    if i not in res:
        res += i

res = ''.join(sorted(res))
if res == alphabet:
    print('YES')
else:
    print('NO')
