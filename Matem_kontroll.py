from random import *
from math import *
from keyboard import *
print("Teadmiste kontroll".center(60,"*"))
tase=0
while tase not in [1,2,3]:
    try:
        tase=int(input("Vali tase (1,2,3): "))        
    except BaseException:
        print("Ainult 1,2 või 3!")# kui format oli vale
    except ValueError:
        print("Noh!,Ainult 1,2 või 3!")
if tase==1:
    min=2
    max=10
    tehed=["+","-"]
elif tase==2:
    min=2
    max=15
    tehed=["+","-","*"]
else:
    min=-20
    max=20
    tehed=["+","-","*","//"]
p=0
kokku=0
while True:    
    v=input("Kas jätkame? esc-lõpp, space-jätkame")
    if v=='stop':
        break
    else:
        kokku+=1
        a=randint(min,max)# !=0 kui //
        b=randint(min,max)# !=0
        tehe=choice(tehed)# 
        if tehe=="//":
            while b==0:
                try:
                    b=randint(min,max)
                except:
                    ValueError
        print(f"{a}{tehe}{b}", end=" ")
        vaja=eval(str(a)+tehe+str(b)) #round()?
        vastus=""
        while type(vastus)!=int:
            try:
                vastus=int(input("="))   # !=str  
            except ValueError:
                print("Vaja int !!!")
        if vastus==int(vaja):
             print("Õige vastus!")
             p+=1
        else:
             print("Mõtle veel!")
print("Kokku ülesandeid oli: ",kokku)
print("Õigev vastused: ",p)
K=(p/kokku)*100
if K<60:
    print("Hinne 2")
elif 60<=K<75:
    print("Hinne 3")