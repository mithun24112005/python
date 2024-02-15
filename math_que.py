import random
import time

operators=["+","-","//","*"]
mino=3
maxo=12
tot_prob=10

def generate_problem():
    left=random.randint(mino,maxo)
    right=random.randint(mino,maxo)
    op=random.choice(operators)

    expr=str(left)+" "+op+" "+str(right)
    ans=eval(expr) #eval function can evaluate the equation without using the if else statement
    return expr,ans
expr,ans=generate_problem()
# print(expr,"=",ans)

wrong=0
input("press enter to start!")
print("-----------------------------------")
start_time=time.time()

for i in range(tot_prob):
    expr,ans=generate_problem()
    while True:
        guess=input("problem #"+str(i+1)+" : "+expr+" = ")
        if guess == str(ans):
            break
        wrong+=1
end_time=time.time()
total_time=round(end_time-start_time,2)
print("-----------------------------------")
print("nice work!! you finished in", total_time, "seconds!")


