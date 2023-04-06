n = int(input())
res_list = []
for i in range(n):
    word = input()
    if len(word) > 10:
        res_list.append(f'{word[0]}{len(word)-2}{word[-1]}')
    else:
        res_list.append(word)

for i in range(len(res_list)):
    print(res_list[i])