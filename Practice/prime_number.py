

# This function will take input from the user and tell whether the given number is Prime or not .

       # 	Prime Numbers
       # Prime numbers are numbers that have only 2 factors: 1 and themselves.
       
       # Negative numbers are not Prime numbers
       
       # 2 is only even prime number 
       
       # This function will run for all negative,positive ,2(the only even prime number)







num = int(input("Enter any num : "))
if num < 0:                                         #if num is less than one means negative it will print the bellow statement
    print("Negative numbers can not be prime")

elif num == 2:                                      # if num is equal to 2 than it will print the bellow statement
    print("2 is only even prime number")
else:                        #if the condition does not satisfies above two conditions than the else statement will be execute
    for i in range(2,num):  # this loop will start from 2 (because every number is divisible by 1 so we will iterate from2) 
        if num % i == 0:     # the input number will divided by i means i will start from 2 and end at (num-1)
            print("Not a prime number") # if the above condition will be True than This will be printed
            break                       # if the condition is true than the loop will be stop !
        elif num % i !=0:            # the above (if) condition will False than this elif condition will be execute
            print("Prime number") 
            break                   # if the (elif) codition will be True than the loop will stop !
            
            
            
         # if we not include the break condition  than it will execute print statement till the loop iterartion will end that's why we will include the break statement
