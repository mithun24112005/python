def task():
    tasks=[]
    print("-------WELCOME TO THE TASK MANAGEMENT APP-------")
    total_task=int(input("enter how many tak u want to add:"))
    for i in range(total_task):
        task_name=input(f"enter task{i+1}: ")
        tasks.append(task_name)
    print(f"today's tasks are\n{tasks}")

    while True:
        operation = int(input("Enter 1-add\n2-update\n3-delete\n4-view\n5-exit : "))
        if operation==1:
            add=input("enter the task u want to add: ")
            tasks.append(add)
        elif operation==2:
            updated_ind=int(input("enter the index of task u want to update:"))
            if tasks[updated_ind] in tasks:
                up=input("enter new task: ")
                tasks[updated_ind]=up
                print(f"updated task {tasks[updated_ind]}")
        elif operation ==3:
            del_ind=int(input("enter the index of task u want to del: "))
            if tasks[del_ind] in tasks:
                del tasks[del_ind]
                print(f"task {tasks[del_ind]} has been deleted..")
        elif operation==4:
            print(f"total tasks: {tasks}")
        elif operation==5:
            print("exiting the program....")
            exit()

task()
# ask input again if entered index is worng in del and update operation
# make it look more pretty
# add functionality to put it in a text file 