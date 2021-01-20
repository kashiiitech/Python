"""function that takes two parameters, one is a list and the other is a number. The function finds the
divisors of the number in the list and prints them. Your function should print “No divisors found” for
number if its divisors are found in the list."""


def lst_divisor(lst,num): 
    divisors = []       # this empty list store the divisors from the list
    for i in lst:
        if(i%num==0): 
            divisors.append(i)
    for divisor in divisors:
        print (divisor)
    if len(divisors)==0:
        print("No divisor Found")
