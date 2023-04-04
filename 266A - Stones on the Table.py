n = int(input())
colors = input()

l = 0
r = 1
c = 0
while r < len(colors):
    if colors[r] == colors[l]:
        c += 1
    else:
        l = r
    r += 1
print(c)