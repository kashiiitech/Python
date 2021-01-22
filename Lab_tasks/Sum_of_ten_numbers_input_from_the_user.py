# Programe that calculate 10 inputs from the user and calculate the sum of all the  numbers 

# If user input the negative number it does not include into the sum .

# Simply skip the negative numbers .



listt = []

loop_end = 1

summ = 0

while loop_end:
    
    num = int(input("Enter your num : "))
    
    listt.append(num)
    
    if loop_end == 10:
        
        break
        
    else:
        
        loop_end+=1
        
for number in listt:
    
    if number < 0:
        
        print("It is negative number so it can not be include !",number)
        
        continue
        
        
        
        
        
 # This program take input from the user that how many times do you want to calculate the numbers

# and than ask the user whether you want to calculate Addition or you want to calculate Multiplication 

# If user select Addition than the programe will calculate the Addition of all numbers

# If user select Multipliction the programe will calculate the Multiplication of all the numbers

# If user give negative values as input than this program will skip the negative values

# This program will run for positive values
        
        
        
        
listt = []
loop_end = 1
summ = 0
multiplication = 1
end = int(input("How many numbers do you want to calculate"))
while loop_end:
    num = int(input("Enter your num : ")) 
    listt.append(num)
    if loop_end == end:
        break
    else:
        loop_end+=1
print("Please select what do you want to calculate \n1.Addition\n2.Multiplication")
selection = int(input())
print()
if selection == 1:
    for number in listt:
        if number < 0:
            print("It is negative number so it can not be include !",number)
            continue
        summ += number
    print("\nThe Sum of all numbers is : ",summ)
elif selection == 2:
    for number in listt:
        if number < 0:
            print("It is negative number so it can not be include !",number)
            continue
        multiplication *= number
    print("\nThe Multiplication of all numbers is : ",multiplication)        
    summ += number
    
print("The sum of all numbers is : ",summ)
    
