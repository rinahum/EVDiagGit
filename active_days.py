import json
"""
Takes the path to the file and 
returns a sorted list with the 
10 most active days
"""
def active_days(file_path):
    days = {}
    with open(file_path, 'r') as f:
        for jsonData in f:
            data = json.loads(jsonData);
            date = data["date"].split("T")[0]
            if(date not in days):
                days[date] = {
                    "date": date,
                    "count": 0
                }
            else:
                days[date]["count"] += 1

    top_days = [None]*10
    for date in days:
        for i in range(len(top_days)):
            if(top_days[i] == None):
                top_days[i] = days[date];
                break;
            elif(top_days[i]["count"] < days[date]["count"]):
                temp_date = top_days[i];
                top_days[i] = days[date];
                for k in range(i + 1, 10):
                    temp = top_days[k];
                    top_days[k] = temp_date;
                    temp_date = temp;
                break;
    for i in range(len(top_days)):
        top_days[i] = top_days[i]["date"];
    
    return top_days

active_days("data/farmers-protest-tweets-2021-03-5.json")