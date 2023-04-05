str1 = input()

msg = 'hello'
res = ''
c = 0
for i in range(len(str1)):
    if str1[i] == msg[c]:
        c+=1
    
print(c)