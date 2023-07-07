#User inputs
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

#Housing Variables
portion_down_payment = 0.25 * total_cost
r = 0.04
monthly_salary = (annual_salary)/12

#Initializing Values
current_savings = 0
months = 0

#Loop to calculate the months it will take to save for the down payment
while (current_savings < portion_down_payment):
    current_savings += (current_savings * (r/12)) + (portion_saved * monthly_salary)
    months += 1
    if (months % 6 == 0):
        monthly_salary += (monthly_salary * semi_annual_raise)
    else:
        monthly_salary = monthly_salary

print("Number of months: ", months)