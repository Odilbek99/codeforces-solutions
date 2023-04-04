def football():    
    inp = input()

    l = 0
    r = 1
    c = 1
    while r < len(inp):
        
        if inp[l] == inp[r]:
            c += 1
        else:
            c = 1
            l = r
        r+=1

        if c >= 7:
            return 'YES'
        
    return 'NO'

f = football()
print(f)
 