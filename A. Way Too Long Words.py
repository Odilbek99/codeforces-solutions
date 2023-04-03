n = int(input())
for i in range(n):
    word = input()
    if len(word) > 10:
        print(f'{word[0]}{len(word)}{word[-1]}')
    else:
        print(word)