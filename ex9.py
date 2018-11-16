#"Random numbers guessing game - ex.9"
import random

exit = input('Type "exit" to quit:')
b = 0
b = random.randint(1, 9)
x = 0
while exit != "exit":
    a = input("Enter a number between 1-9 or exit to quit: ")
    if (a == "exit"):
        print("Program exiting\n")
        break

    x += 1
    if (int(a) < b):
        print("Too low. Try again!\n")
    elif (int(a) > b):
        print("Too high. Try again!\n")
    else:
        print("Right On!")
        x=0
        b=random.randint(1, 9)
        print("It took you", x, "tries!\n")