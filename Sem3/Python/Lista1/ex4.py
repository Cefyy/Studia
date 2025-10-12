#Załóżmy kwadrat 400x400 i wpisane koło o środku w punkcie (0,0)
import random
import math

def pi():
    epsilon = 1e-6
    tries = 10000
    radius= 200
    ltwo=0
    cltwt=0
    our_pi=0
    while(tries > 0 and abs(math.pi-our_pi)>epsilon):
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        distance = math.sqrt(x**2+y**2)
        if(distance <= radius):
            ltwo+=1
        cltwt+=1
        tries-=1
        our_pi = (4*ltwo)/cltwt
        print(our_pi)
        
        
pi()