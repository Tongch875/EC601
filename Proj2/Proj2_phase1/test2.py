# !/usr/bin/env python
from TwitterAPI import TwitterAPI
from TwitterAPI import TwitterPager

import tweepy  # https://github.com/tweepy/tweepy
import json

# Twitter API credentials
consumer_key = "ncUtdcz60tY0gpLcFvtWBNRnB" #"Enter the consumer_key"
consumer_secret = "tuFCAQqAKfc3ffbnuEDasRJyGBDSnf32L6GncTmIUNePZLzc08"# Enter the consumer_secret"
access_key = "1440796131798118401-hFSAtnwkbXj8DMMA7o4Rf4C5f1lj7Y"#Enter the access_key"
access_secret = "HShMTj1Y16bjhEB8AS7c9YYQ9hWuEu9TNUPgHiVPueaYn"#Enter the access_secret"


def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=20)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    i = 1

    # Print tweets of the user by timeline
    for tweet in new_tweets:
        print(str(i) + '. ' + tweet.text + '\n')
        i = i + 1

    public_tweets = api.user_timeline(screen_name=screen_name, user_id="BU_Tweets", count=20)
    for tweet in public_tweets:
        print(str(i) + '. ' + tweet.text + '\n')
        i = i + 1

    # keep grabbing tweets until there are no tweets left to grab
    # while len(new_tweets) > 0:
    #
    #     # all subsiquent requests use the max_id param to prevent duplicates
    #     new_tweets = api.user_timeline(screen_name=screen_name, count=10, max_id=oldest)
    #
    #     # save most recent tweets
    #     alltweets.extend(new_tweets)
    #
    #     # update the id of the oldest tweet less one
    #     oldest = alltweets[-1].id - 1
    #     if (len(alltweets) > 15):
    #         break
    #     print
    #     "...%s tweets downloaded so far" % (len(alltweets))
    #
    # # write tweet objects to JSON
    # file = open('tweet.json', 'w')
    # print
    # "Writing tweet objects to JSON please wait..."
    # for status in alltweets:
    #     json.dump(status._json, file, sort_keys=True, indent=4)
    #
    # # close the file
    # print
    # "Done"
    # file.close()


if __name__ == '__main__':
    # pass in the username of the account you want to download
    get_all_tweets("@TONGCHA35960567")  #"@Ibra_official"