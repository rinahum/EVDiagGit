import json
"""
Takes the path to the file and 
returns a sorted list with the 
10 most used hashtags
"""
def top_hashtags(file_path):
    hashtags = {}
    with open(file_path, 'r') as f:
        for jsonData in f:
            data = json.loads(jsonData);
            slices = data["content"].split(" ");
            for slice in slices:
                if "#" in slice:
                    hashtag = slice
                    if(hashtag not in hashtags):
                        hashtags[hashtag] = {
                            "hashtag": hashtag,
                            "count": 1
                        }
                    else:
                        hashtags[hashtag]["count"] += 1
    top_hashtags = [None]*10
    for hashtag in hashtags:
        for i in range(len(top_hashtags)):
            if(top_hashtags[i] == None):
                top_hashtags[i] = hashtags[hashtag];
                break;
            elif(top_hashtags[i]["count"] < hashtags[hashtag]["count"]):
                temp_hashtag = top_hashtags[i];
                top_hashtags[i] = hashtags[hashtag];
                for k in range(i + 1, 10):
                    temp = top_hashtags[k];
                    top_hashtags[k] = temp_hashtag;
                    temp_hashtag = temp;
                break;
    for i in range(len(top_hashtags)):
        top_hashtags[i] = top_hashtags[i]["hashtag"];

    return 0
top_hashtags("data/farmers-protest-tweets-2021-03-5.json")