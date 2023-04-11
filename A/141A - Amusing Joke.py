s1 = input()
s2 = input()
s3 = input()

s12 = sorted(s1+s2)
s3 = sorted(s3)
if s12 == s3:
    print('YES')
else:
    print('NO')