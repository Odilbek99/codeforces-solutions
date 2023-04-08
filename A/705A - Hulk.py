n = int(input())

t1 = 'I hate'
t2 = 'I love'
that = ' that '
it = ' it'
res = ''
if n == 1:
    print(t1+it)
else:
    for i in range(1,n+1):

        if i % 2 != 0 and i != n:
            res += t1 + that
        elif i % 2 == 0 and i != n:
            res += t2 + that 
        else:
            if i%2 == 0:
                res += t2 + it
            else:
                res += t1 + it
    print(res)

            
        