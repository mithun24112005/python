import os

def creat_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"filename {filename}: created successfully!")
    except FileExistsError:
        print(f"{filename} already exists")
    except Exception as e:
        print("an error occored")

def view_all_files():
    files=os.listdir()
    if not files:
        print("no file found")
    else:
        print("files in directory are:")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted")
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print("an error occured!")

def read_file(filename):
    try:
        with open(filename,'r') as f:
            content=f.read()
            print(f"content of {filename}: \n{content}")
    except FileNotFoundError:
        print(f"{filename} not found")
    except Exception as e:
        print("an error occured")

def edit_file(filename):
    try:
        with open(filename,'a') as f:
            content=input("enter data to add: ")
            f.write(content+"\n")
            print(f"content added to {filename}")
    except FileNotFoundError:
        print(f"{filename} not found")
    except Exception as e:
        print("an error occured")

def main():
    while True:
        print("-------------FILE MANAGEMENT APP-----------")
        print('1:Create file')
        print('2:View all files')
        print('3:delete files')
        print('4:read files')
        print('5:edit file')
        print('6:exit')

        choice=input("enter the choice:")
        if choice=='1':
            filename=input("enter the filename to create: ")
            creat_file(filename)
        elif choice=='2':
            view_all_files()
        elif choice=='3':
            filename=input("enter the filename u wnat to delete: ")
            delete_file(filename)
        elif choice=='4':
            filename=input("enter the filename to read: ")
            read_file(filename)
        elif choice=='5':
            filename=input("enter the filename to edit: ")
            edit_file(filename)
        elif choice=='6':
            print("exiting program....")
            exit()
        else:
            print("invalid choice.... try again..")

if __name__=="__main__":
    main()