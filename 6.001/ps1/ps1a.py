#User inputs
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home: "))

#Housing Variables
portion_down_payment = 0.25 * total_cost
r = 0.04
monthly_salary = (annual_salary)/12

#Initial Values
current_savings = 0
months = 0

#Loop to calculate the months it will take to save for the down payment
while (current_savings < portion_down_payment):
    current_savings += (current_savings * (r/12)) + (portion_saved * monthly_salary)
    months += 1

print("Number of months: ", months)