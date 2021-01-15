#  Write a function that takes a list as a parameter and returns the second maximum in the list. Assuming
#  the list consists of only integers.

# This code will work when the list is given only positive values


def sec_max(lst):
    result = 0
    maxx = max(lst)
    minn = min(lst)
    for i in lst:
        if (i>minn) and (i<maxx):
            result = i
    return result
    
    
    
    
    # This code will run for all positive and negative values
    
    
    
def sec_max(lst):
    for x in range(0,len(lst)):
        for j in range(x,len(lst)):
            if lst[x]>lst[j]:
                lst[x],lst[j] = lst[j],lst[x]  
    result = 0
    maxx = max(lst)
    minn = min(lst)
    for i in lst:
        if (i>minn) and (i<maxx):
            result = i
    return result
