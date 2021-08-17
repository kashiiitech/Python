# Question No 2

def length(num):                    # here we define the function
    s = str(num)			# we can convert the num into the string
    length=0                     # it will calculate the length of the number
    for i in s:                  # this loop will iterate from 0 to the last digit of the number
        length+=1                # in every iteration 1 will be added to the length variable
        
    return length       # in last here we return the length of the num to the function call
        
