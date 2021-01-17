"""function that inserts a value in
the list at its proper position (index) such that after inserting the value the list is still sorted. The list can
either be in ascending or descending order, your function should work for both types. You can write a
separate function to which would tell you in which order the list is sorted (Hint: You only have to check
the first two numbers to determine in which order the list is sorted)."""



#  it must have two parameters: first the list you want to insert and second the value in

#  which you want to insert the value. (You are not allowed to use the sort function of lists)






def proper_index(lst,num):
    lst.append(num)
    if lst[0]<lst[1]:
        for i in range(0,len(lst)+1):
            for j in range(i,len(lst)):
                if lst[i]>lst[j]:
                    lst[i],lst[j] = lst[j],lst[i]
                    
    elif lst[0]>lst[1]:
        for i in range(0,len(lst)+1):
            for j in range(i,len(lst)):
                if lst[i]<lst[j]:
                    lst[i],lst[j] = lst[j],lst[i]
    return lst
