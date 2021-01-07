"""
#PART A
annual_salary = float(input("Enter your annual salary: "))
prop_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home: "))
annual_ret = 0.04
portion_down_payment = 0.25 * total_cost
current_savings = 0
months = 0

while current_savings < (0.25 * total_cost):
    months += 1
    inv_returns = current_savings*(annual_ret/12)
    current_savings += prop_saved * (annual_salary/12)
    current_savings += inv_returns
print(f"Number of months: {months}")

#Both test cases correct


#PART B - With 6-month raises
annual_salary = float(input("Annual salary: "))
prop_saved = float(input("Proportion saved: "))
total_cost = float(input("Cost of dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))
annual_ret = 0.04
portion_down_payment = 0.25 * total_cost
current_savings = 0
months = 0

while current_savings < (0.25 * total_cost):
    months += 1
    inv_returns = current_savings*(annual_ret/12)
    current_savings += prop_saved * (annual_salary/12)
    current_savings += inv_returns
    if months%6 == 0:
        annual_salary = annual_salary*(1+semi_annual_raise)
print(months)

#All three test cases correct.


#Part C - Finding the right amount of money to save away

#finding the best savings rate through teh bisection method. 
#Assumptions: dreamhouse price is $1m, 25% downpayment, semi_annual 
#raise is 0.07, annual return of investments is 0.04, want dwpmnt within
#36 months

import math
possibilities = [x for x in range(0,10001)]
starting_salary = float(input("Enter the starting salary: "))
num_bisections = 0
#other vars as given in the question
annual_return = 0.04
semi_annual_raise = 0.07
total_cost = 1000000
downpayment_prop = 0.25

j=0
while True:
    j += 1
    mid_point = math.ceil((possibilities[0] + possibilities[-1])/2)
    print(f"midpoint is {mid_point}")
    #work out how much they'd save in the given timeframe, then compare, 
    #and adjust range (discard half)
    savings = 0
    months = 0
    for i in range(0,36+1):
        months += 1
        investment_returns = savings * (annual_return/12)
        savings += investment_returns + (mid_point/100)*(starting_salary/12)
        if i%6 ==0:
            starting_salary = (1+semi_annual_raise)*starting_salary
    if abs(savings-total_cost) < 100:
        print(f"Best savings rate: {mid_point/100}")
        print(f"Steps in bisection search: {num_bisections}")
        break
    else:
        if savings > downpayment_prop * total_cost: #remove midpt and above
            possibilities = possibilities[0:possibilities.index(mid_point)]
        else:
            possibilities = possibilities[possibilities.index(mid_point):]
        num_bisections+=1
    if j==3:
        break
        


possibilities = [x for x in range(0,10001)]

import math
for i in range(5):
    print(i)
    mdpt = math.ceil((possibilities[0] + possibilities[-1])/2)
    print(f"{mdpt} is the midpoint.")
    possibilities = possibilities[possibilities.index(mdpt):]
    print(len(possibilities))
    
"""


import math
possibilities = [x for x in range(0,10000+1)]
total_price = 1000000
deposit_prop = 0.25
annual_return = 0.04
semi_annual_raise = 0.07
deposit_needed = deposit_prop * total_price
bisections = 0
starting_salary = float(input("Enter the starting salary: "))

while True:
    savings = 0
    print("savings = zero")
    midpoint = math.ceil((possibilities[0]+possibilities[-1])/2)
    print(f"mdpt: {midpoint}")
    for month in range(0, 36+1):
        investment_returns = savings * (annual_return/12)
        monthly_wage = starting_salary/12
        savings += (midpoint/10000) * (monthly_wage) + investment_returns
        if month%6 == 0 and month>1:
            starting_salary *= (1+semi_annual_raise)
        else:
            ()
    if abs(savings - deposit_needed) <= 100:
        break
    elif savings > deposit_needed: #saved too much, so "optimal" saving rate below midpt
        possibilities = possibilities[0:possibilities.index(midpoint)]
        print("Saved up too much!")
    else:
        print("Saved up too little!")
        possibilities = possibilities[possibilities.index(midpoint):len(possibilities)]
    bisections += 1
    print(f"Savings: {savings}")
    savings = 0

print(f"Best savings rate: {midpoint/1000}")
print(f"Steps in bisection search: {bisections}")
    