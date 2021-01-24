"""function should be called “get_countries”. This function will also be
given a list of dictionaries, however, it has to return a dictionary. Each key in the
dictionary is a distinct country in the given list. The value of each key is the
number of companies in the country represented by the key."""





def get_countries(company):
    dictionary = dict()       # Here we define a empty dictionary .
    for dic in company:      # this will take a dictionary in company list 
        for key in dic:      # this will take keys from dictionary .
            if key == "Country":    # if key is equal to country than the condition become True .
                country_name = dic[key]   # this will take country name and than assign it into the country_name variable .
                if country_name in dictionary:  # this will check if it is avvailable in dictionary or not
                    dictionary[country_name]+= 1 #if it is available than simply this add one to the value againt country name
                else:                         # if the country name is not available than this will add the country name .
                    dictionary[country_name] = 1  # this will add country name in dictionary and than give 1 as its value .
    return dictionary   
    
    # Here we return the dictionary in last the dictionary have number of countries that how many a country occur in dictionary this will count the countries . s
