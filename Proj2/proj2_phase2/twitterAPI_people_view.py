#具体找和某个人相关的评论，别人对他的评论
def people_view():
    import tweepy
    import json
    import sys

    # input the keys and secret to acquire permission of API
    consumerKey = ""
    consumerSecret = ""
    accessToken = ""
    accessTokenSecret = ""
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth)

    KEY = input(" Input KEYWORDS that you want to find: ")
    NUM = int(input("Input the NUMBER that you need : "))

    LIST = []  # creat a new list to save data

    search = tweepy.Cursor(api.search_tweets, KEY).items(NUM)  # use the API of search

    for tweets in search:
        LIST.append([username(tweets.text) ,tweets.text]) # alltweets.text #tweets.id

    # print("This is what you want to find :")
    # for i in LIST:
    #     print(i)

    return LIST, KEY

def username(text):
    start = text.find("@")
    end = text.find(":")
    name = text[start:end]
    return name
