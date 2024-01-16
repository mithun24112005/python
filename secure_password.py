# Create a python program to secure an existing password by
# replacing a set of characters with the corresponding
# •password-secure' character (Provided as tuple) .
# Example:
# SECURE = (('s',"$"),("and","&"),("a","@"),("o","0"),("i","1"),("I","|"))
# Input :
# password = "Indians123"
# Output :
# Your secure password is Ind1@n$123

# used to make secure and memorable password


SECURE=(('s', "$"), ('and', '&'), ('a', '@'), ('o', '0'), ('i', '1'), ('I', '|'), ('E', '3'), ('t', '+'), ('b', '6'), ('g', '9'),('H','#'))

def securepass(password):
    for a,b in SECURE:
        password=password.replace(a,b)
    return password

if __name__=="__main__":
    password=input("enter your password: ")
    password=securepass(password)
    print(f"your secure password is {password}")
