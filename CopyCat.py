#this is the main function of the program
def copycat():
    user_input = input("Please enter a string here: ")
    print(user_input)

#this prints the messege and calls the function
print("This program is made to print what the user inputs!")
copycat()

while True:
    choice = input('''
1: Enter another string
2: Exit the program

Please select an option: ''')

#if the user enters anything exept a number the program will reask to enter
    try:
        choice = int(choice)
        if choice not in [1, 2]:
            print("Invalid option selected. Please choose option 1 or 2.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        copycat()
    else:
        print("Goodbye!")
        break
