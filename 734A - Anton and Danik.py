n = int(input())
winners = input()

a = winners.count('A')
d = winners.count('D')

if a > d:
    print('Anton')
elif a < d:
    print('Danik')
else:
    print('Friendship')