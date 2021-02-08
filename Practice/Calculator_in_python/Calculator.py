"""A simple calculator with a menu. Display the following options
to the user, prompt for a selection, and carry out the requested action
(e.g. prompt for two numbers and add them). After each operation, return
the user to the menu. Exit the program when the user selects 0. If the user
enters a number which is not in the menu, ignore the input and redisplay
the menu. You can assume that the user will enter a valid integer """

#      -- Calculator Menu --

#	0. Quit
#	1. Add two numbers
#	2. Subtract two numbers
#	3. Multiply two numbers
#	4. Divide two numbers
#   5. Average of two numbers


try:
    while True:
        print("\n\tCalculator Menu")
        print("\t0.Quit\n\t1.Add two numbers\n\t2.Subtract two numbers\n\t3.Multiply two numbers\n\t4.Divide two numbers\n\t5.Average of two numbers")
        selection = int(input("\nSelect :"))
        if selection == 0:
            break
        num1 = int(input("Enter your first number : "))
        num2 = int(input("Enter your second number : "))
    
        if selection == 1:
            print("\t=",num1+num2)
        elif selection == 2:
            print("\t=",num1-num2)
        elif selection == 3:
            print("=\t",num1*num2)
        elif selection == 4:
            if num2 == 0:
                print("\n \tCan not divided by zero")
            else:
                print("\t=",num1/num2)
        elif selection == 5:
            print("\t=",(num1+num2)/2)
        
        
except ValueError:
    print("\n\tWrite only integers")
