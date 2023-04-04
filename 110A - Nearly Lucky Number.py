n = input()

seven = n.count('7')
four = n.count('4')

sum_ = seven+four
if (str(sum_) == '7' or str(sum_) == '4'):
    print('YES')
else:
    print('NO')

