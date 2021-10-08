# 情感分析，找到近期和你对某个人物同样情感的人
# Imports the Google Cloud client library
from google.cloud import language_v1
import twitterAPI_people_view
import stars_themself

# Instantiates a client
from twitterAPI_people_view import people_view
import past_tweets

client = language_v1.LanguageServiceClient()

# The text to analyze
# text = u"Hello, world!"
# KEY = input(" Input KEYWORDS that you want to find: ")
LIST , KEY= people_view()    #!!!!!!!
group_positive = []
group_negative = []
group_neutral = []
for i in range(len(LIST)):
    id_text = LIST[i][1]

    document = language_v1.Document(content=id_text, type_=language_v1.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
    LIST[i].append([sentiment.score, sentiment.magnitude])
    if sentiment.score > 0:
        group_positive.append(LIST[i] )
    elif sentiment.score == 0:
        group_neutral.append(LIST[i] )
    else:
        group_negative.append(LIST[i] )

    print("Text: {}".format(id_text))
    print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))

print("-------------------------------------------------------")
print("positive:")
for i in group_positive:
    print(i)
print("neutral:")
for i in group_neutral:
    print(i)
print("negative:")
for i in group_negative:
    print(i)

support_rate = len(group_positive)/len(LIST)
print()
print("support rate: ", support_rate)
print()

print("positive group history last 100 tweets")
for i in range(len(group_positive)):
    name=group_positive[i][0]
    if len(name)>0:
        personal_tweets = past_tweets.get_personal_tweets(name, KEY)
        print(name)
        for j in personal_tweets:
            print(j)

