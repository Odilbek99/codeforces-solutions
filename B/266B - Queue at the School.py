n, t = map(int, input().split())
str1 = list(input())

l = 0
r = 1
c = 0
for i in range(t):
    while r < n:
        if str1[l] == "B" and str1[r] == 'G':
            str1[l],str1[r] = str1[r], str1[l]
            l = r+1
        else:
            l = r
        
        r+=1

    l = 0
    r = 1

print(''.join(str1))