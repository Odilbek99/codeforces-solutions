str1 = list(map(str, input().lower()))
vowels = 'aoyeui'
res = ''
for i in range(len(str1)):
    if str1[i] not in vowels:
        res += '.'
        res += str1[i]
print(res)