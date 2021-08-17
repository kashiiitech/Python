# Question no 3

def array(lst):
    lst1 = []
    lst2 = []
    summ = 0
    k = 0
    for i in range(0,len(lst)):
        for j in lst:
            lst1.append(j[i])
    
    import copy
    lst2.append(copy.deepcopy(lst1))
    lst1.clear()
    k+=1
    lst3 = []
    for i in lst2:
        for j in i:
            summ += j
        lst3.append(summ)
        summ=0
    return max(lst3)
