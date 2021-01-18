
#This program take input from the user and then calculate the table of given number


#   Solution No1
  #  By using for loop .


num = int(input("Enter Any Num : "))   # take input from the user 
for i in range(1,11):                  # loop iterate from 1 to 10
    print(i,"x",num,"=",i*num)      # multiply given num to the i (i start from 1 and finish at 10)
    
    
    #   Solution No 2
    
    #  By using while loop
    
multiplier = 1                        # variable 
num = int(input("Enter Any Num : "))   #   take input from the user 
while multiplier < 11:                # here this loop will iterate till the given condition becomes false
    print(multiplier,"x",num,"=",num*multiplier)  # here we multiply the number given from user to the multiplier 
    multiplier += 1      # in every iteration of loop one will added to the multiplier till 11 than the condition become False and loop will be finish !
