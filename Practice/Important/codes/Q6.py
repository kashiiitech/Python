#Write a function that takes an integer as a parameter and returns the sum of digits in that integer.



def sum_integer(x):  
    y = str(x)        # Here we change type of number from integer to string
    summ = 0          
    for i in y:      # this loop will take every digit from the string in every iteration
        i = int(i)   # the type of i is string so here we change into the integer
        summ += i  # here the variable named summ has initially zero but in every iterartion the i will be added to the summ and tha assign into the summ .
    return summ    # in last the sum of all digits is in the variable summ here we return it to the function from where it is called .
