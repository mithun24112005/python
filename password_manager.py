# store password and encript it 
from cryptography.fernet import Fernet

def load_key():
    file = open("key.key","rb")
    key=file.read()
    file.close()
    return key

# master_pwd=input("what is the master password?: ")
key=load_key() #+ master_pwd.encode()
fer=Fernet(key)

'''def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)'''

# write_key()


def view():
    with open('passwords.txt','r') as f: 
        for line in f.readlines():
            data=line.rstrip() # rstrip --> removes the \n when displayed
            user,passw=data.split("|")  # split --> it will split whenevr it sees the charecter in the list form
            print("User:", user, "| password:", fer.decrypt(passw.encode()).decode())

def add():
    name=input("account name: ")
    pwd=input("password: ")
    with open('passwords.txt','a') as f: 
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode=input("would u like to add a password or view it or quit the program(view,add,q)?: ").lower()
    if mode=="q":
        break
    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("invalid mode")
        continue

