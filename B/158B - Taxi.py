n = int(input())
line = list(map(int,input().split()))
 
three = line.count(3)
two = line.count(2)
one = line.count(1)

ans = line.count(4)

if three >= one:
    print(three + ans + (two+1)//2)
else:
    ans+=three
    one-=three
    if two%2==0:
        print((one+3)//4 + ans + two//2)
    else:
        print((one+2+3)//4+ans+two//2)
