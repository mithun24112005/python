import random
l=int(input("enter the length of the password: "))
cha='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz()*&%$#!@'
password=""
for i in range(l):
    password+=random.choice(cha)
print(password)
