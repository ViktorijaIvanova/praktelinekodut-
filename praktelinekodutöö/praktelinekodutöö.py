#harjutus
from math import*
from random import*
x=int()
s=0
pr=1
maksimaalselt=3
miinimum=0
while x>0:
    viimane=x%10
    miinimum=miinimum+1
    if viimane%2==0:
        maksimaalselt+=1
    s=s+viimane
    pr=pr*viimane 
    if viimane>maksimaalselt:
        maksimaalselt=viimane 
    if viimane>miinimum:
        miinimum=viimane 
    x=x//10
print("sööge minimaalne arv kordi",miinimum)
print ("sööge maksimaalselt arv kordi",maksimaalselt)
print ("kõigi aegade summa",s)
print ("kõigi aegade  korrutama",pr)






#harjutus 8
a = 1
while a < 101:
    print("Tsükkel lõpetatud", a, "aeg(a)")
    a = a+1
print("tsükkel on lõpp")


#задача я хожу в тех пока не наступают выходные через while or for
