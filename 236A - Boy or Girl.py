name = input()
n_char = len(set(name))
if n_char % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')