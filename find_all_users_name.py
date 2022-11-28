from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    users=data['messages']
    l=[]
    for i in users:
        if i.get('actor','none')!='none':
            l+=[i['actor']]
    l1=list(set(l)) 
    return l1
data = read_data('data/result.json')
print(find_all_users_name(data))
