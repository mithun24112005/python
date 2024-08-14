# multi clipboard

import sys
import clipboard
import json
SAVED_DATA="clipboard.json"
# clipboard.copy("abc")
# data=clipboard.paste()
# print(data)

# print(sys.argv[1:]) # it gives the list of commands passed after the keyword python in terminal

# creating a json file
def save_data(filepath,data):
    with open(filepath,"w") as f:
        json.dump(data,f)

def load_data(filepath):
    try:
        with open(filepath,"r") as f:
            data=json.load(f)
            return data
    except:
        return {}

if len(sys.argv)==2:
    command=sys.argv[1]
    # print(command)
    data=load_data(SAVED_DATA)
    # save command inputs the key and assigns the copied text to that key and writes in the json file in form of dictionary
    if command=="save":
        key=input("enter a key: ")
        data[key]=clipboard.paste()
        save_data(SAVED_DATA,data)
        print("data saved")
    # load command loads the value of the key to the clipboard
    elif command=="load":
        key=input("enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("data copied to clipboard")
        else:
            print("key does not exist")
    elif command=="list":
        print(data)
    else:
        print("unknown command")
else:
    print("please pass exactly one command")