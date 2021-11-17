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
        a=randint(min,max)
        b=randint(min,max)
        tehe=choice(tehed)#
        print(f"{a}{tehe}{b}", end=" ")
        vaja=eval(str(a)+tehe+str(b)) #round()?
        vastus=int(input("="))               
        if vastus==int(vaja):
             print("Õige vastus!")
             p+=1
        else:
             print("Mõtle veel!")