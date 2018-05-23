print("""This is a basic game for the purpose of learning Python.
--------------------
You are at a crossroad.""")

choice_1 = True
while choice_1 == True:
    answer_1 = input("Do you want to go right, or left?: ")
    if answer_1 == "right" or answer_1 == "Right":
        print("You turned right at the crossroad.")
        choice_1 = False
    if answer_1 == "left" or answer_1 == "Left":
        print ("You turned left at the crossroad.")
        choice_1 = False
    else:
        print("Invalid input")