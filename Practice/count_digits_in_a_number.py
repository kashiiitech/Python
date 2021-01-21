#Given a number count the total number of digits in a number



def count_digits_in_num(num):
    if num < 1:                # this block will run when the number is less than 1
        y = str(-1*num)
        summ = 0
        for i in y:
            summ += 1
        return summ
    
    elif num > 1:           # this will run when the num is greater than 1
         
        y = str(num)
        summ = 0
        for i in y:
            summ += 1
        return summ
