s = list(map(str,input().split('WUB')))
res = ''
for word in s:
    if word != '':
        res += word + ' '
print(res)
# print(' '.join(s.split('WUB')))