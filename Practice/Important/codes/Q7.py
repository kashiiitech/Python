# function that takes an integer as a parameter. The function finds the number of even, odd and
#  zero digits in the integer.




def integer_count(x):
    y = str(x)
    counter1 = 0
    counter2 = 0
    counter3 = 0
    for i in y:
        i = int(i)
        if (i>0):
            if (i%2==0):
                counter1+=1
        if not(i%2==0):
            counter2+=1
        elif i == 0:
            counter3+=1
    print("Number of even : ",counter1)
    print("Number of odd : ",counter2)
    print("Number of zero : ",counter3)
