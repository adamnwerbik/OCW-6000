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
    discriminant = (b**2 - 4*a*c)/(2*a)
    if discriminant < 0:
        return "Error: Roots are complex"
    elif discriminant == 0:
        return (-b/(2*a))
    else:
        return ((-b + math.sqrt(b**2 - 4*a*c))/(2*a), (-b - math.sqrt(b**2 - 4*a*c))/(2*a))



print(roots(1, 2, 3))
print(roots(1, 2, -3))
print(roots(1, 2, 1))


#Skipped 2.6 & 2.7


#Ex 2.8
def report_card():
    num_subjects = int(input("How many subjects did you take: "))
    subject_db = dict()
    total = 0
    for subject in range(num_subjects):
        name = input("What was the name of this subject?: ")
        mark = int(input(f"What was your grade for {name}?: "))
        #print("Mark is " + str(mark))
        total += mark
        subject_db[name] = mark
    print("REPORT CARD")
    for i in subject_db:
        print(i +": " + str(subject_db[i]))
    print("Overall GPA: " + str(total/int(num_subjects)))
#report_card()

#Ex 2.9
def pig_latin(word):
    vowels = ['a','e','i','o','u']
    pig_latin_word = ""
    if word[0] in vowels:
        return word + "hay"
    else:
        first_letter = word[0]
        return word[1:] + first_letter + "ay"

print(pig_latin("image"))
print(pig_latin("boot"))
print(pig_latin("adamwerbik"))

#Ex. 2.10 - List Comprehensions
nums_1_to_10_cubed = [x**3 for x in range(1,10+1)]

coin_flips = [x+y for x in ["h", "t"] for y in ["h", "t"]]

def get_vowels(string):
    vowels = ['a','e','i','o','u']
    return [x for x in string if x in vowels]

print(get_vowels("Adam Werbik"))