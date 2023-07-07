cheer = input("What do you want to cheer for? ").upper()
length = len(cheer)

for char in cheer:
    if char in 'AEFHLMORSX':
        article = 'an'
    else:
        article = 'a'
    print("Give me " + article + " " + char + "!" + " " + char + "!")

for i in range(length):
    print(cheer + "!")