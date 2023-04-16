def copycat():
    user_input = input("Please enter a string here: ")
    print(user_input)

print("This program is made to print what the user inputs!")
copycat()

choice = input(''' 
1: Enter another string
2: Exit the program

Please select a option:
    ''')

if choice == '1':
    copycat()
else:
    print("Goodbye!")
    exit
