'''
Created on 2022/10/14

@author: t20cs052
'''
import random

def te(n):
    if n==0:
        return "ぐー"
    elif n==1:
        return "ちょき"
    elif n==2:
        return "ぱー"
   
'''
a = random.randint(0,2)
b = random.randint(0,2)
c = random.uniform(0,2)
d = random.random()
'''
a=0
b=2
print('Aのて:',te(a))
print('Bのて:',te(b))

if a==b:
    print("あいこ")
    
elif a<b and (a==0 and b==2):
    print("Aの勝利")
else:
    print("Bの勝利")