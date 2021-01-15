#Write a function that takes an integer as a parameter and returns the sum of digits in that integer.



def sum_integer(x):
    y = str(x)
    summ = 0
    for i in y:
        i = int(i)
        summ += i
    return summ
