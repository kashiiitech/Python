# Write a python function to calculate the factorial of a number .


def factorial_count(fac):
    factorial = 1
    if(fac<0):
        return print("The factorial of negative number does not exists")
    elif (fac==0):
        return print("The factorial of zero is 1 ")
    else:
        for i in range(1,fac+1):
            factorial = (factorial * i)
    return factorial
    
    
    
    
 # Now modify this to take the input from the user and pass into the function as a parameter
 
 fac = int(input("Enter Any Num : "))
def factorial_count(fac):
    factorial = 1
    if (fac<0):
        return print("The factorial of negative number does not exist")
    elif (fac==0):
        return print("The factorial of zero is 1")
    else:
        for i in range(1,fac+1):
            factorial = (factorial*i)
    return factorial
    
    
factorial_count(fac)
