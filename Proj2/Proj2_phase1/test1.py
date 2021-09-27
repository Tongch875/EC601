# !/usr/bin/env python
import tweepy  # https://github.com/tweepy/tweepy
import json

from TwitterAPI import TwitterAPI
from TwitterAPI import TwitterPager

# Twitter API credentials
consumer_key = "ncUtdcz60tY0gpLcFvtWBNRnB" #"Enter the consumer_key"
consumer_secret = "tuFCAQqAKfc3ffbnuEDasRJyGBDSnf32L6GncTmIUNePZLzc08"# Enter the consumer_secret"
access_key = "1440796131798118401-hFSAtnwkbXj8DMMA7o4Rf4C5f1lj7Y"#Enter the access_key"
access_secret = "HShMTj1Y16bjhEB8AS7c9YYQ9hWuEu9TNUPgHiVPueaYn"#Enter the access_secret"

api = TwitterAPI(consumer_key,
                 consumer_secret,
                 access_key,
                 access_secret)

#获取你最近的 50 条推文 RECENT 50 TWEETS
r = api.request('statuses/home_timeline', {'count':50})
for item in r.get_iterator():
    if 'text' in item:
        print (item['text'])

print("--------------------------------------------------------")

#获取整个时间线TIMELINE
pager = TwitterPager(api, 'statuses/home_timeline', {'count':200})
for item in pager.get_iterator(wait=60):
    if 'text' in item:
        print (item['text'])

#发一条推文TWEET
r = api.request('statuses/update', {'status': 'Its time to go to sleep!'})
print ('SUCCESS') if r.status_code == 200 else 'FAILURE'

#发布带有图片的推文 add PIC
# STEP 1 - upload image
file = open('./20200705_121049.jpg', 'rb')
#C:/Users/TONG CHANG/PycharmProjects/pythonProject
data = file.read()
r = api.request('media/upload', None, {'media': data})
print('UPLOAD MEDIA SUCCESS' if r.status_code == 200 else 'UPLOAD MEDIA FAILURE')

# STEP 2 - post tweet with reference to uploaded image
if r.status_code == 200:
        media_id = r.json()['media_id']
        r = api.request('statuses/update', {'status':'PIC test!', 'media_ids':media_id})
        print('UPDATE STATUS SUCCESS' if r.status_code == 200 else 'UPDATE STATUS FAILURE')

#删除推文DELETE
# r = api.request('statuses/destroy/:%d' % TWEET_ID)
# print ('SUCCESS') if r.status_code == 200 else 'FAILURE'