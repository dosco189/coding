name = input("Enter your name: ")
dob = input("date of birth dd/mm/yyyy: ")

a, b, c = dob.split("/") 
age = 2023 - int(c)

print("Congratulations, you're", age, "years old", name, "!")
