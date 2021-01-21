
# This function take input from the user and than pass into the function .

# the output is the reverse of the number .


# This will run for both positive and negative integers


num = int(input("Enter any positive or negative number : "))
def reverse_a_given_integer_num(num):
    if num < 0:
        num = -1*num
        y = str(num)
        k = ""
        for i in range(len(y)-1,-1,-1):
            k = k+y[i]
            out_num = int(k)
        return out_num*-1
    else:   
        y = str(num)
        k = ""
        for i in range(len(y)-1,-1,-1):
            k = k+y[i]
        return int(k)
reverse_a_given_integer_num(num)
