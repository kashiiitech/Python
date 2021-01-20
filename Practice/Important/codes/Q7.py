# function that takes an integer as a parameter. The function finds the number of even, odd and
#  zero digits in the integer.




def evens_odds_zeros_count(num):
    y = str(num)
    evens = 0
    odds = 0   
    zeros = 0
    for i in y:
        i = int(i)
        if (i>0):
            if (i%2==0):
                evens+=1
        if not(i%2==0):
            odds+=1
        elif i == 0:
            zeros+=1
    print("Number of even : ",evens)
    print("Number of odd : ",odds)
    print("Number of zero : ",zeros)
