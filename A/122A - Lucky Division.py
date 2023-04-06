s = int(input())
bool_ = True
for i in set(str(s)):
    if i == '4' or i == '7':
        continue
    else:
        bool_ = False

if bool_ == False:
    
    if s%4 == 0 or s%7 == 0:
        print('YES')
    else:
        print('NO')
else:
    print('YES')