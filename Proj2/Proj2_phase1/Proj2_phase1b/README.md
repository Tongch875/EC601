# Google API

## Tong Chang

I installed the Google cloud SDK shell according to Google’s instructions.I create API keys and save them in environment variables so that I don’t need to insert the API key value every time I call the API. In Google cloud SDK shell the detailed analysis for each word is given. Part of it is like this：

"mentions": [
        {
          "text": {
            "beginOffset": 0,
            "content": "Michelangelo Caravaggio"
          },
          "type": "PROPER"
        },
        {
          "text": {
            "beginOffset": 33,
            "content": "painter"
          },
          "type": "COMMON"
        }
      ],
      "metadata": {
        "mid": "/m/020bg",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Caravaggio"
      },
      "name": "Michelangelo Caravaggio",
      "salience": 0.82904786,
      "type": "PERSON"
      
A very detailed and thorough analysis and search of a person’s name.

I also run sentiment analysis programs from Python. For clear sentences, Google’s sentiment analysis is very accurate. However, for sentences with complex meanings, such as satire, Google's analysis is sometimes not very accurate.

Text: The more people I know, the more I like dogs. 
Sentiment: 0.5, 0.5
Text:  It does not matter if you are single, you will still be single in the future!
Sentiment: 0.8999999761581421, 0.8999999761581421
Text:  His teeth are like stars in the sky, bright in color and far apart.
Sentiment: 0.800000011920929, 0.800000011920929

Normally, the meanings of these three sentences or want to express are negative. That is to say, the first parameter of emotion, sentiment.score, should be negative. But Google recognizes them as positive.

