"""function you need to write is called “get_companies”. It takes the list of
dictionaries representing companies along with a dictionary representing
location. This dictionary will have “City” and “Country” as its keys. The values of
these keys can be any strings. Your function should return a list of companies
which are located in the location provided as a dictionary to the function."""



def get_companies(company,location):
    listt = []                    
    for keyy in location:       # this will take key of location that is provided
        for dic in company:     # this will take dictionaries from list .
            for key,value in list(dic.items()): # this will make a list in which first element is key and second is value of 							  #	dictionaries and assign into variables the key to key variable and 								# value to value variable
                if value == location[keyy]:    # if value of dictionary is equal to the value of location .
                	listt.append(dic["Company Name"])  # than the company name of that location is assign to listt
        break                                            # if one time it is assign than this will break(stop) the loop .
    if len(listt)==0:  # if the length of listt is 0 than this means the location is invalid so it will return None
        return 'None'
    return listt     # if the location is in dictionaries than this will return the list of company names .
