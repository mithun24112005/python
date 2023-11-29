import string
import random

s = []
pw = ""
password = []
op=[0,1]
len = int(input("enter the length of the password: "))
lowle = string.ascii_lowercase
uple = string.ascii_uppercase
digits = string.digits
spchar = string.punctuation
low = int(input("do u want lower case letters 0 or 1: "))
upp = int(input("do u want upper case letters 0 or 1: "))
num = int(input("do u want numbers in password 0 or 1: "))
spch = int(input("do u want special charecters 0 or 1: "))

if(low and upp and num and spch in op):
    if low == 1:
        s.extend(lowle)
    if upp == 1:
        s.extend(uple)
    if num == 1:
        s.extend(digits)
    if spch == 1:
        s.extend(spchar)
    for i in range(len):
        pw += random.choice(s)
else:
    print("invalid input.")
    quit()

print(pw)
