#具体找和某个人相关的评论，别人对他的评论
def people_view():
    import tweepy
    import json
    import sys

    # input the keys and secret to acquire permission of API
    consumerKey = "ncUtdcz60tY0gpLcFvtWBNRnB"# "5cQw8mSauZEG5A4Frn2uMQrnk"
    consumerSecret = "tuFCAQqAKfc3ffbnuEDasRJyGBDSnf32L6GncTmIUNePZLzc08"
    #"Ig1myJTZOR5VF2HMezfVd2n33ZfhSIWbYUpuBfiBfSEuvwto1y"
    accessToken = "1440796131798118401-hFSAtnwkbXj8DMMA7o4Rf4C5f1lj7Y"
    #"1441983537008152581-tPEF6LEkZIuSfEKSc9AhBVs8tj023Y"
    accessTokenSecret = "HShMTj1Y16bjhEB8AS7c9YYQ9hWuEu9TNUPgHiVPueaYn"
    #"f65k2QiGQEBOvHIbVIAfU0MjTZJfLg2FMVHZcKkQqhi1M"
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
