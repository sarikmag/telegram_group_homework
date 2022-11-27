from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    users=data['messages']
    s=0
    for i in users:
        if i.get('actor_id','none')!='none':
            if i['actor_id']==users_id and i['type']=='message':
                s+=1

    return s
print(find_user_message_count(read_data('data/result.json'),'user646113348'))