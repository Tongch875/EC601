import tweepy  # https://github.com/tweepy/tweepy
import json

# Twitter API credentials
consumer_key = ""  # "Enter the consumer_key"
consumer_secret = ""  # Enter the consumer_secret"
access_key = ""  # Enter the access_key"
access_secret = ""  # Enter the access_secret"


def get_personal_tweets(name, KEY):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets---------------------------
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(user_id=name, count=100)

    i = 1

    # Print tweets of the user by timeline
    for tweet in new_tweets:
        LIST=[]
        words= tweet.text
        if words.find(KEY) >= 0:
            text = str(i) + '. ' + tweet.text
            LIST.append(text)
            # print(str(i) + '. ' + tweet.text + '\n')
            i = i + 1
    return LIST

    # -------------------------------
    # NUM = 50
    # search = tweepy.Cursor(api.search_tweets, KEY ).items(NUM)  # use the API of search
    # # search = api.search_tweets(q=KEY, count=200)
    # LIST = []
    # for tweets in search:
    #     LIST.append([tweets.id, tweets.text])  # alltweets.text
    #
    # print("This is what you want to find :")
    # for i in LIST:
    #     print(i)

    # return LIST


if __name__ == '__main__':
    # pass in the username of the account you want to download
    # print("@BarackObama")
    get_personal_tweets("@BarackObama", "obama")
