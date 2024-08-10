# def intreverse(n):
#     str_n = str(n)
#     reversed_str_n = str_n[::-1]
#     reversed_n = int(reversed_str_n)
#     return reversed_n

# num=8731873
# print(intreverse(num))

# def matched(s):
#     open_count=0
#     for i in s:
#         if i=='(':
#             open_count+=1
#         elif i==')':
#             open_count-=1
#             if open_count<0:
#                 return False
#     if open_count!=0:
#         return False
#     else:
#         return True
# print(matched("((jkl)78(A)&l(8(dd(FJI:),):)?)"))

def is_prime(a):
    if a<=0:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True
def sumprimes(l):
    b=[]
    for i in l:
        if is_prime(i)==True:
            b.append(i)
    summ=0
    for i in b:
        summ+=i
    return summ


# print(sum([12,23,21,3,12]))
print(sumprimes([17,51,29,39]))
print(is_prime(39))

