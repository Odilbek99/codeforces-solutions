a = int(input())
b = int(input())
c = int(input())

expr_list = [a*b*c,a+b+c,a+b*c,(a+b)*c,a*b+c,a*(b+c)]
print(max(expr_list))
