num1 = input()
num2 = input()

res = ''
for i in range(len(num1)):
    if num1[i] != num2[i]:
        res += str(1)
    else:
        res += str(0)

print(res)