"""function that takes two parameters, one is a list and the other is a number. The function finds the
divisors of the number in the list and prints them. Your function should print “No divisors found” for
number if its divisors are found in the list."""


def lst_divisor(x,num):
    for i in x:
        if(i%num==0):
            print(i)
    else:
        print("No Divisor Found")
