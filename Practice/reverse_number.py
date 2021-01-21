# Reverse a given number and return true if it is the same as the original number .

def reverse_num(num):
    y = str(num)
    k = ""
    for l in range(len(y)-1,-1,-1):
        k = k+y[l]
        if k == y:
            return True
    else:
        return False
