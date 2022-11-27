from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    users=data['messages']
    l=[]
    for i in users:
        if i.get('actor_id','none')!='none':
            if i['actor_id'][0:4]=='user':
                l+=[i['actor_id']]
    l1=list(set(l))
    return l1
print(find_all_users_id(read_data("data/result.json")))