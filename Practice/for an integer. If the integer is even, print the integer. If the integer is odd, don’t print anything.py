"""Write a program which repeatedly prompts the user for an integer. If the integer is even, print the integer. If the integer is odd, don’t print anything. Exit the program if the user enters the integer 99."""


while True:
    inputt = int(input("enter num : "))
    if inputt%2==0:
        print(inputt)
    elif inputt == 99:
        break
    elif inputt%2!=0:
        print()
            
