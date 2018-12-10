import csv

import tweepy

consumer_key = '4XlzJCHVEg9ZktElJhCKPwPYZ'
consumer_secret = 'V6uwFSUw5LH4A086tzvgeP3d2IfKzuPWmWHtNocucNL46DouHu'
access_token = '975658194331725825-VqN2wbElxgO6jQfmnA0paW7jBmAhJcV'
access_secret = 'LPmCT4SFCafdaabNZzVeFY1IG7s4bSRmcNLnGynwxS6BC'

# connexion à l'API twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


with open('negative_tweet.txt', 'w') as csvfile:
  csv_writer = csv.writer(csvfile)
  csv_writer.writerow(["Sentiment " "Tweet_Id"])
  csvfile.close()


f = open('id_tweet.gold_neg.txt', 'r')
while 1:
    data = f.readline()
    try:
        datat = data[9:27]
        tweets = api.get_status(datat)
        tweet = tweets.text
        print(tweet)
        with open('negative_tweet.txt', 'a') as csvfile:

           csvfile.writelines({

            tweet
        })
    except Exception as e:
           pass