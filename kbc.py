ques=[["which lang is used to create fb?","python","c++","c","js",4],["which lang is used to create fb?","python","c++","c","js",4],["which lang is used to create fb?","python","c++","c","js",4],["which lang is used to create fb?","python","c++","c","js",4],["which lang is used to create fb?","python","c++","c","js",4],["which lang is used to create fb?","python","c++","c","js",4]]
levels=[1000,2000,3000,10000,50000,320000]
money=0
for i in range(0,len(ques)):
    que=ques[i]
    print(f"question for Rs.{levels[i]}")
    print(que[0])
    print(f"a.{que[1]}\t\tb.{que[2]}\nc.{que[3]}\t\td.{que[4]}")
    reply=int(input("enter ur option(1-4) or 0 to quit: "))
    if reply==0:
        print(f"the money u won: {levels[i-1]}")
        break
    elif reply==que[-1]:
        print(f"correct ans, u have won Rs.{levels[i]}")
        if(i==3):
            money=10000
        elif i==5:
            money=320000
            
    else:
        print("wrong ans!!")
        print(f"the total money u win: {money}")
        break
