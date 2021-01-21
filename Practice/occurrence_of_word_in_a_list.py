
# The function take list as a parameter and return a dictionary

# in dictionary there is occurence of words that how many times a word occured in the list

# this function count the occurence of each word in dictionary 

def word_occurrence_count(lst):
    dictionary = dict()
    for i in lst:
        if i in dictionary:
            dictionary[i]+=1
        else:
            dictionary[i]=1
    return dictionary
