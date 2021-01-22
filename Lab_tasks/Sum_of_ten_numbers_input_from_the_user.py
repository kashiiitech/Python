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
        
    summ += number
    
print("The sum of all numbers is : ",summ)
    
