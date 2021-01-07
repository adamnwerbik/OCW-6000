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
starting_salary = float(input("Enter the starting salary: "))
num_bisections = 0
#finding the best savings rate through teh bisection method. 
#Assumptions: dreamhouse price is $1m, 25% downpayment, semi_annual 
#raise is 0.07, annual return of investments is 0.04, want dwpmnt within
#36 months

possibilities = [x for x in range(0,10001)]
num_bisections = 0
annual_salary = float(input("Enter your annual salary: "))
while True:
    mid_point = (possibilities[0] + possibilities[-1])/2
    print(f"midpoint is {mid_point}")
    #work out how much they'd save in the given timeframe, then compare, 
    #and adjust range (discard half)
    savings = 0
    for i in range(0,36+1):
        investment_returns = savings * (0.04/12)
        savings += investment_returns + annual_salary 
        



    if saved_up
    

mid_point = (possibilities[0] + possibilities[-1])/2
print(f"midpoint is {mid_point}")
saving_proportion = 
