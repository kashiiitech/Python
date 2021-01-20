#  Write a function that takes a list as a parameter and reverses the list without using the built-in reverse
#  function.




def reverse_list(lst):
    lst_reverse_elements = []
    for i in range(len(lst)-1,-1,-1):
        lst_reverse_elements.append(lst[i])
    lst.clear()
    for j in lst_reverse_elements:
        lst.append(j)
    return lst



# Second simple logic

def reverse_list(lst):
    list_reverse = []
    for i in range(len(lst)-1,-1,-1):
        list_reverse.append(lst[i])
    return list_reverse
    
