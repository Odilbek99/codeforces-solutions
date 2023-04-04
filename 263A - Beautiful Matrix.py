pos_1 = None
for i in range(5):
    row = list(map(int, input().split()))
    if 1 in row:
        pos_1 = (i,row.index(1))

calc = abs(pos_1[0]-2) + abs(pos_1[1]-2)
print(calc)
