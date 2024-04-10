# take name and time for watching the video
# and save in txt file

import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            test=json.load(file) #loads the file
            # print(type(test))
            return test
    except FileNotFoundError:
        return []

def save_data_helper(video):
    with open('youtube.txt','w') as file:
        json.dump(video,file) #takes data and file name to dump the given data

def list_all_vid(video):
    print("\n")
    print("*"*70)
    for index,video in enumerate(video,start=1):
        print(f"{index}. {video["name"]}, duration: {video["time"]}")
    print("*"*70)

def add_vid(video):
    name=input("enter the name of video: ")
    time=input("enter the time u need: ")
    video.append({'name':name,'time':time})
    save_data_helper(video)

def update_vid(video):
    list_all_vid(video)
    index=int(input("enter the vid num to update: "))
    if 1<=index<=len(video):
        name=input("enter the vid name: ")
        time=input("enter the time u need: ")
        video[index-1]={"name":name,"time":time}
        save_data_helper(video)
        print("your list is updated")
    else:
        print("invalid index")

def del_vid(video):
    list_all_vid(video)
    index=int(input("entre the vid num to be deleted: "))
    if 1<=index<=len(video):
        del video[index-1]
        save_data_helper(video)
        print("your list is updated")
    else:
        print("invalid index")

def main():
    video=load_data()
    while True:
        print("\nYoutube Manager | choose an option: ")
        print("1) list a fav video")
        print("2) add a youtube video")
        print("3) update a youtube video details")
        print("4) delete youtube video")
        print("5) exit the app")
        choice=int(input("enter your choice: "))
        # print(video)

        match choice:
            case 1:
                list_all_vid(video)
            case 2:
                add_vid(video)
            case 3:
                update_vid(video)
            case 4:
                del_vid(video)
            case 5:
                quit()
            case _:
                print("invalid choice")
                continue

if __name__=="__main__":
    main()



