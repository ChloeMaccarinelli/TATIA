import csv
import re
import string

from nltk import PorterStemmer, TweetTokenizer
from nltk.corpus import stopwords

import tweepy

consumer_key = '4XlzJCHVEg9ZktElJhCKPwPYZ'
consumer_secret = 'V6uwFSUw5LH4A086tzvgeP3d2IfKzuPWmWHtNocucNL46DouHu'
access_token = '975658194331725825-VqN2wbElxgO6jQfmnA0paW7jBmAhJcV'
access_secret = 'LPmCT4SFCafdaabNZzVeFY1IG7s4bSRmcNLnGynwxS6BC'

# connexion à l'API twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Happy Emoticons
emoticons_happy = set([
    ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
    ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
    '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
    'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
    '<3'
])

# Sad Emoticons
emoticons_sad = set([
    ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
    ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
    ':c', ':{', '>:\\', ';('
])

# all emoticons (happy + sad)
emoticons = emoticons_happy.union(emoticons_sad)

stopwords_english = stopwords.words('english')
stemmer = PorterStemmer()


def clean_tweets(tweet):
    # remove hyperlinks
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)

    # remove hashtags
    # only removing the hash # sign from the word
    tweet = re.sub('#[\w\.\-]+', '', tweet)
    tweet = re.sub('@[\w\.\-]+', '', tweet)

    # tokenize tweets
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    tweet_tokens = tokenizer.tokenize(tweet)
    tweets_clean = []
    for word in tweet_tokens:
        if (word not in stopwords_english and  # remove stopwords
                word not in string.punctuation and
                word not in emoticons):
            stem_word = stemmer.stem(word)  # stemming word
            tweets_clean.append(stem_word)
    return tweets_clean

neutral = 0
pos =0
neg = 0
neut = 0

with open('Sentiment_Analysis_polarity_class_mots.txt', 'w') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Sentiment " "Tweet_Id"])
    csvfile.close()
f = open('id_tweets.input.txt', 'r')
while 1:
    data = f.readline()
    if not data:
        break
    else :
        try:
            tweets = api.get_status(data)
            tweet = tweets.text
            print("tweet de base => " + tweet)

            words = clean_tweets(tweet)
            print(words)
            listeNeg = []
            with open('negativeWords.txt','r') as n :
                neg = n.readline()
                for word in words:
                    for neg in n :
                        if word in neg :
                            listeNeg.append(word)

            print(listeNeg.__len__())

            listePos=[]
            with open('positiveWords.txt','r') as n :
                pos = n.readline()
                for word in words:
                    for pos in n :
                        if word in pos :
                            listePos.append(word)

            print(listePos.__len__())

            if listeNeg.__len__() == listePos.__len__() :
                neutral = 1

            print(neutral)

            neutral = 0
            words.clear()

            classify = "neutral"
            if listeNeg.__len__() < listePos.__len__():
                classify = "positive"
            elif listeNeg.__len__() > listePos.__len__():
                classify ="negative"

            with open('Sentiment_Analysis_polarity_class_mots.txt', 'a') as csvfile:

                csvfile.writelines({

                    classify + " " +data
                })



        except Exception as e:

            with open('exceptions.txt', 'a') as file:

                file.writelines({

                    data
                })


