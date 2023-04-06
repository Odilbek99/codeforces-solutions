str1 = input()

msg = 'hello'

c = 0
res = ''
for char in msg:
    for i in range(c,len(str1)):
        c += 1
        if char == str1[i]:
            res += str1[i]
            break
if res == msg:
    print('YES')
else:
    print('NO')
    
        

