def HCF(x,y):
    while(x):
        x,y = y,y%x
        return y
