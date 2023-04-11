n,m = map(int,input().split())

c = 0
for i in range(1,n+1):
    
    if i%2 == 0:
        c+=1
        if c%2 == 0:
            print('#'+'.'*(m-1))
        else:
            print('.'*(m-1)+'#')
    else:
        print('#'*m)
    