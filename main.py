from pymongo import MongoClient

dbClient = MongoClient('mongodb://localhost:27017/')

dbOrigin = dbClient['filter1']
dbDest = dbClient['filter2']

videoCollection = dbOrigin['videos']
reactionCollection = dbDest['reaction']

testVideo = videoCollection.find_one({"_id": "JMUhaCXPyg8"})
comments = testVideo['topLevelComment']

for comment in comments:

    reaction = {
    }

    if "love" in comment['text']:
        print("A GOOD REACTION")
        reaction['type'] = "positive"
    elif "great" in comment['text']:
        print("A GOOD REACTION")
        reaction['type'] = "positive"
    elif "good" in comment['text']:
        print("A GOOD REACTION")
        reaction['type'] = "positive"
    elif "i like" in comment['text']:
        print("A GOOD REACTION")
        reaction['type'] = "positive"
    elif "i liked" in comment['text']:
        print("A GOOD REACTION")
        reaction['type'] = "positive"
    elif "racist" in comment['text']:
        print("A DISCUSSION REACTION")
        reaction['type'] = "discussion"
    elif "racism" in comment['text']:
        print("A DISCUSSION REACTION")
        reaction['type'] = "discussion"
    elif "don't like" in comment['text']:
        print("A NEGATIVE REACTION")
        reaction['type'] = "negative"
    elif "dont like" in comment['text']:
        print("A NEGATIVE REACTION")
        reaction['type'] = "negative"
    elif "is bad" in comment['text']:
        print("A NEGATIVE REACTION")
        reaction['type'] = "negative"
    elif "didn't like" in comment['text']:
        print("A NEGATIVE REACTION")
        reaction['type'] = "negative"
    elif "didnt like" in comment['text']:
        print("A NEGATIVE REACTION")
        reaction['type'] = "negative"
    elif "hate" in comment['text']:
        print("A NEGATIVE REACTION")
        reaction['type'] = "negative"
    elif "hated" in comment['text']:
        print("A NEGATIVE REACTION")
        reaction['type'] = "negative"
    elif "bad" in comment['text']:
        print("A NEGATIVE REACTION")
        reaction['type'] = "negative"
    else:
        print("NEUTRAL REACTION")
        reaction['type'] = "neutral"

    reaction['author'] = comment['author']

    reactionCollection.insert_one(reaction)

print("ENDED TEST")
