import os

def isbinod(filename):
    with open(filename,'r') as f:
        filecontent=f.read()
    if "binod" in filecontent.lower():
        return True
    else:
        return False

#listing the contents of this folder
dirc=os.listdir()
print(dirc)
nbinod=0
#for each text file run isbinod for them
for item in dirc:
    if item.endswith('txt'):
        print(f"detecting binod in {item}")
        flag=isbinod(item)
        if (flag==True):
            print(f"binod found in {item}")
            nbinod+=1
        else:
            print(f"binod not found in {item}")
print("********binod detector summary*********")
print(f"{nbinod} files found with binod into them")