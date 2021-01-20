#function that takes two lists and returns True if they have at least one common member.



def common_data(list1, list2):
    result = False
    for x in list1:
         for y in list2:
                 if x == y:
                    result = True
    return result



# Second Logic


def common_member(lst1,lst2):
    for i in lst1:
        for j in lst2:
            if i == j:        # here first i will take first value of lst1 and comapare all values of lst 2 if it equal than return True
                return True
    else:
        return False
    
    
    
    # Third Logic
    
    
    def common_member(lst1,lst2):
    for i in lst1:
        if i in lst2:      # here i will take every value of lst1 and check it in lst2 if it is available than it return True else it return False
            return True
    else:
        return False
