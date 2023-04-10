n,m = map(int,input().split())
line = list(map(int,input().split()))
line.sort()
l = 0
r = n

min_ = None
while r <= m:
    print(line[l:r+1])
    if min_ != None:
        min_ = min(min_,max(line[l:r])-min(line[l:r]))
        
    else:
        
        min_ = max(line[l:r])-min(line[l:r])
    
    l+=1
    r+=1

print(min_)
