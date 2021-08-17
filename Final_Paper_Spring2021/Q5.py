# Question No 5


def is_disarium(num):   # define a function to check the number is desarium or not
    st = str(num)       # here we convert the given num in the string
    lst = []            # this will append all the numbers individualy to the list
    for i in st:        # this loop will take one digit of the number in i
        lst.append(int(i))  # this will convert the number from string to int and then append to the 	list
        
      # This logic is for check whether the number is disarium or not
    j = 1
    summ = 0
    for i in lst:
        summ += (i**j)
        j+=1
    if (num==summ):
        return True
    else:
        return False
