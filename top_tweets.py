import json
"""
Takes the path to the file and 
returns a sorted list with the 
10 most retweeted tweets
"""
def top_tweets(file_path):
    tweets = [None]*10;
    with open(file_path, 'r') as f:
        for jsonData in f:
            #Parses the file line to a json
            data = json.loads(jsonData);

            for i in range(len(tweets)):
                if(tweets[i] == None):
                    tweets[i] = data;
                    break;
                elif(tweets[i]["retweetCount"] < data["retweetCount"]):
                    # Adds the value and shifts the list to the right
                    temp_tweet = tweets[i];
                    tweets[i] = data;
                    for k in range(i + 1, 10):
                        temp = tweets[k];
                        tweets[k] = temp_tweet;
                        temp_tweet = temp;
                    break;
    return tweets;