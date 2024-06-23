print('''
                          
                        ,d     
                        88     
,adPPYYba, 8b,dPPYba, MM88MMM  
""     `Y8 88P'   `"8a  88     
,adPPPPP88 88       88  88     
88,    ,88 88       88  88,    
`"8bbdP"Y8 88       88  "Y888  
      ''')

print("Welcome to the Ant Game. Your mission - should you choose to accept it - is to help the ant find its way out of the maze.")
print("The ant is currently at an impasse. It can either go left or right. Which way should it go?")
choice = input("Type 'left' or 'right' and hit 'Enter'.").lower()
if choice == "left":
    print("The ant has chosen to go left. It has encountered a river. It can either swim across or wait and go back. What should it do?")
    swim_choice = input("Type 'swim' or 'wait' and hit 'Enter'.").lower()
    if swim_choice == "wait":
        print("The ant has chosen to wait. Patience has its rewards. A fairy appears and offers you three choices of doors to enter. Which one will you choose?")
        final_choice = input("Type 'red', 'blue', or 'yellow' and hit 'Enter'.").lower()
        if final_choice == "yellow":
            print("Congratulations! You have found the exit. You have won the game.")
        else:
            print("Oh no! The ant chose the wrong door. It was a trap. Game Over.")
    else:
        print("Oh no! The ant was eaten by a crocodile while trying to swim across the river. Game Over.")
else:
    print("Oh no! The ant fell into a hole and can't get out. Game Over.")