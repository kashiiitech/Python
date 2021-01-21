
# function that take number as a parameter and calculate the sum of all number between 1 and given number


def sum_num(num):
    if num<1:            # this block will run if the number is less than one .
        khan = []
        summ = 0
        for i in range(num,0):
            khan.append(i)
        for j in khan:
            summ += j
        return summ
    else:           #  this block will run when number is not less than one ( means greater than one ) .
        
    	khan = []
    	summ = 0
    	for i in range(num,-1,-1):
        	khan.append(i)
    	for j in khan:
        	summ += j
    	return summ
    
