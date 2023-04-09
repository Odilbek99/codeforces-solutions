n = int(input())
for i in range(n):
    a,b = map(int,input().split())

    if a < b:
        print(b-a)
    elif a == b or a%b == 0:
        print(0)
    else:
        print(b-(a%b))
