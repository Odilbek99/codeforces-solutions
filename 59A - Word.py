word = input()

up_count = 0
for i in word:
    if i.isupper():
        up_count += 1
low_count = len(word) - up_count
if low_count >= up_count:
    print(word.lower())
else:
    print(word.upper())
