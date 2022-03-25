import json
"""
Takes the path to the file and 
returns a sorted list with the 
10 most active users
"""
def top_users(file_path):
    users = {}
    with open(file_path, 'r') as f:
        for jsonData in f:
            data = json.loads(jsonData);
            user = {
                "user": data["user"],
                "count": 0}
            if(data["user"]["id"] in users):
                users[data["user"]["id"]]["count"] += 1;
            else:
                users[data["user"]["id"]] = user;
    top_users = [None]*10;
    for user in users:
        for i in range(len(top_users)):
            if(top_users[i] == None):
                top_users[i] = users[user];
                break;
            elif(top_users[i]["count"] < users[user]["count"]):
                temp_user = top_users[i];
                top_users[i] = users[user];
                for k in range(i + 1, 10):
                    temp = top_users[k];
                    top_users[k] = temp_user;
                    temp_user = temp;
                break;
    for i in range(len(top_users)):
        top_users[i] = top_users[i]["user"];
    
    return top_users;
top_users("data/farmers-protest-tweets-2021-03-5.json")