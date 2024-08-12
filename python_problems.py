# def intreverse(n):
#     str_n = str(n)
#     reversed_str_n = str_n[::-1]
#     reversed_n = int(reversed_str_n)
#     return reversed_n

# num=8731873
# print(intreverse(num))

####################################################
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

####################################################
# def is_prime(a):
#     if a<=0:
#         return False
#     for i in range(2,int(a**0.5)+1):
#         if a%i==0:
#             return False
#     return True
# def sumprimes(l):
#     b=[]
#     for i in l:
#         if is_prime(i)==True:
#             b.append(i)
#     summ=0
#     for i in b:
#         summ+=i
#     return summ
# # print(sum([12,23,21,3,12]))
# print(sumprimes([17,51,29,39]))
# print(is_prime(39)

####################################################
# sum of first n positive numbers
# n=int(input("enter number: "))
# sum=(n*(n+1))/2
# print(sum)

####################################################
#time of python program excecution
# import time
# def myfunc():
#     start_time=time.time()
#     s=0
#     for i in range(1,n+1):
#         end_time=time.time()
#         return s,end_time-start_time

# n=5
# print(myfunc())

####################################################
# to get current user in python 
# import getpass
# print(getpass.getuser())

####################################################
# access environment variables
# import os
# print(os.environ)

####################################################
# list all files in a directory
# from os import listdir
# from os.path import isfile,join
# files_list=[f for f in listdir('/Home')if isfile(join('/Users',f))]

####################################################
# check for leap year
# year=int(input("enter the year to be checked: "))
# if year%400==0 and year%100==0:
#     print("it is a leap year")
# elif year%4==0 and year%100!=0:
#     print("it is a leap year")
# else:
#     print("not a leap year")

####################################################
# allprime numbers between range
# a=int(input("enter the start range:"))
# b=int(input("enter the end range:"))
# print("this is the list of prime numbers:")
# for i in range(a,b+1):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)

####################################################
# armstrong number in interval
# def armstrong(num):
#     order = len(str(num))
#     copy = num
#     total = 0
#     i = 0
#     while i < order:
#         digit = num % 10
#         total += digit ** order
#         num = num // 10
#         i += 1
#     if total == copy:
#         return True
#     return False

# start = int(input("Enter starting number of the interval: "))
# end = int(input("Enter ending number of the interval: "))

# print(f"Armstrong numbers in the interval [{start}, {end}]:")
# for i in range(start, end + 1):
#     if armstrong(i):
#         print(i)

####################################################
# anonomous func is lambda func
# display powers of 2 using map,lambda
# n=int(input("enter the number of terms: "))
# result=list(map(lambda x: 2**x,range(n+1)))
# print(result)

####################################################
# Find Numbers Divisible by Another Number
# lower=int(input("enter lower limit: "))
# upper=int(input("enter upper limit: "))
# a=int(input("enter the number to be divided with: "))
# print(f"here are the numbers divisible by {a}")
# # for i in range(lower,upper):
# #     if i%a==0:
# #         print(i)
# print(list(filter(lambda x: x%a==0,range(lower,upper))))

####################################################
# convert num to octal,hexa,binary
# dec=int(input("enter a decimal num:"))
# print(bin(dec), ":in binary")
# print(oct(dec), ":in octal")
# print(hex(dec), ":in hexa")

####################################################
# find ascii valie of char
# a=input("enter a char:")
# print(ord(a))

####################################################
# to find the factors of a num
# num=int(input("enter the num:"))
# l=[]
# for i in range(1,num+1):
#     if num%i==0:
#         l.append(i)
# print(f"these r the factors of {num}: {l}")

####################################################
# shuffle deck of card
# import random,itertools
# deck=list(itertools.product(range(1,14),["spade","club","heart","diamond"]))
# # print(deck)
# random.shuffle(deck)
# for i in range(5):
#     print(deck[i])

####################################################
# program to display calender
# import calendar
# year=int(input("enter the year: "))
# month=int(input("enter the month no:"))
# calendar=calendar.month(year,month)
# print(calendar)

####################################################

