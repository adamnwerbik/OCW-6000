# Exercise 2.2

def is_divisible(m, n):
    return (m % n == 0)

#test cases
print(is_divisible(30,1)) #should return True
print(is_divisible(35,2)) #should return False
print(is_divisible(3,50)) #should return False


def not_equal(a, b):
    if type(a) == type(b):
        if a - b == 0:
            return False
        else:
            return True
    else:
        return True

print(not_equal(1,2)) #should return True
print(not_equal(2,2)) #should return False
print(not_equal(2,"2")) #should return True: same as what is returned by print(2 != "2") 

#Exercise 2.3
import math

def multadd(a,b,c):
    return a*b+c

pi = math.pi
angle_test = math.sin(pi/4) + math.cos(pi/4)/2
print(angle_test) #1.0606601717798212: correct

ceiling_test = math.ceil(276/19)+2*math.log(12,7)
print(ceiling_test) #17.55397881653925: correct

def yikes(x):
    return multadd()


#Ex 2.4
import random
def rand_divis_3():
    rand_num = random.randint(0,100)
    print("Random number: " + str(rand_num))
    return rand_num%3==0

print(rand_divis_3())
print(rand_divis_3())
print(rand_divis_3())

def roll_dice(sides, dices):
    rolls = []
    for i in range(1,dices+1):
        rolls.append(random.randint(1, sides))
    return rolls
    
print(roll_dice(6,20))
print(roll_dice(60,1))
print(roll_dice(3,30))

#Exercise 2.5 - Quadratic Formula
def roots(a, b, c):
    determinant = (b**2 - 4*a*c)/(2*a)
    if determinant < 0:
        return "Error: Roots are complex"
    elif determinant = 0:
        
