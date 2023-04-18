n = int(input())

for i in range(n):
    s = int(input())
    df = int('1' + (len(str(s)))*'0')//10

    # print(type(df))
    if 1<= s <=10 or s % df == 0:
        print(1)
        print(s)
    
    else:
        c = 0
        res = ''
        while s != 0:
            c+=1
            res += f'{s-s%df} '
            s = s%df
            df = int('1' + (len(str(s))-1)*'0')
            if s == 0:
                break
            
        print(c)    
        print(res)
        
    
        
    

        

