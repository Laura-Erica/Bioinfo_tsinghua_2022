
import random

#随机产生p1和p2作为起始估计
p1=random.random()
p2=random.random()

print("please enter the number of head in 10 times, separated by space, terminated by enter")
arr=input("")
num=[int(n) for n in arr.split()]

T1=[0,0,0,0,0]
T2=[0,0,0,0,0]
T3=[0,0,0,0,0]
T4=[0,0,0,0,0]

temp1=0
temp2=0
i=0

while True:
    for j in range(5):
        temp1=p1**num[j]*(1-p1)**(10-num[j])/(p1**num[j]*(1-p1)**(10-num[j])+p2**num[j]*(1-p2)**(10-num[j]))
        temp2=1-temp1
        #print(temp1,temp2)
        T1[j] = num[j]*temp1
        T2[j] = (10-num[j])*temp1
        T3[j] = num[j]*temp2
        T4[j] = (10-num[j])*temp2
        i=i+1
        #print(temp1,temp2,T1,T2,T3,T4,num,sep='\n')
    #print(sum(T1),sum(T2),sum(T3),sum(T4))

    temp1=sum(T1)/(sum(T1)+sum(T2))
    temp2=sum(T3)/(sum(T3)+sum(T4))


    if temp1==p1 and temp2==p2:
         print("p1=",round(p1,4),"\n","p2=",round(p2,4),"\n","迭代次数为",i,"\n",sep='')
         break
    else:
        p1=temp1
        p2=temp2

 