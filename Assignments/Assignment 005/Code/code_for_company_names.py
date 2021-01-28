"""function with the name “get_companies_names”. The function will be
given a list of dictionaries following the above specifications. The function should
return a list containing “Company Name” from each dictionary in the given list."""


def get_companies_names(company):
    list_of_company_names = []
    for i in company:
        k = i['Company Name']
        list_of_company_names.append(k)
    return list_of_company_names
