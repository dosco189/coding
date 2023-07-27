def is_even(i):
    """
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    if i%2 == 0:
        print("True")
    else:
        print("False")  

number = int(input("Enter a number: "))
is_even(number)
