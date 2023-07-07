#User inputs
annual_salary = float(input("Enter your annual salary: "))

#Standard Variables
house_cost = 1000000
down_payment = 0.25 * house_cost
r = 0.04
monthly_salary = (annual_salary)/12
semi_annual_raise = 0.07
savings = 0

#Initializing Values
low_value = 0
high_value = 10000
steps = 0

#Calculate the bisecting value for the savings rate
while (abs(savings - down_payment) >= 100):
    guess_rate = (low_value + high_value)/2
    steps += 1
    savings = 0
    monthly_salary = (annual_salary)/12
    for month in range(1,37):
        savings += (savings * (r/12)) + ((guess_rate/10000) * monthly_salary)
        if (month % 6 == 0):
            monthly_salary += (monthly_salary * semi_annual_raise)
        else:
            monthly_salary = monthly_salary
    if (savings < down_payment):
        low_value = guess_rate
    else:
        high_value = guess_rate
    if (guess_rate == 10000):
        break

guess_rate = guess_rate/10000
print("Best savings rate: ", guess_rate)
print("Steps in bisection search: ", steps)