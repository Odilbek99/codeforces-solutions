n = int(input())

l = []

for i in range(n):
    in_, out = map(int, input().split())
    l.append(-in_+out)
res = [sum(l[ : i + 1]) for i in range(len(l))]
print(max(res))
