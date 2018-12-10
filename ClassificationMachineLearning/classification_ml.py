# coding: utf8
import csv
import string

import pandas as pd
import tokenizer as tokenizer
import tweepy

# information API twitter
from nltk import TweetTokenizer, re, PorterStemmer, NaiveBayesClassifier, classify, defaultdict, ConfusionMatrix
from nltk.corpus import stopwords, twitter_samples
from textblob import TextBlob



consumer_key = '4XlzJCHVEg9ZktElJhCKPwPYZ'
consumer_secret = 'V6uwFSUw5LH4A086tzvgeP3d2IfKzuPWmWHtNocucNL46DouHu'
access_token = '975658194331725825-VqN2wbElxgO6jQfmnA0paW7jBmAhJcV'
access_secret = 'LPmCT4SFCafdaabNZzVeFY1IG7s4bSRmcNLnGynwxS6BC'
# connexion à l'API twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)



pos_tweets = twitter_samples.strings('positive_tweets.json')
neg_tweets = twitter_samples.strings('negative_tweets.json')



stopwords_english = stopwords.words('english')

stemmer = PorterStemmer()

tweet_tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)

def clean_tweets(tweet):
    # remove hyperlinks
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)

    # remove hashtags
    # only removing the hash # sign from the word
    tweet = re.sub(r'#', '', tweet)

    # tokenize tweets
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    tweet_tokens = tokenizer.tokenize(tweet)

    tweets_clean = []
    for word in tweet_tokens:
        if (word not in stopwords_english and  # remove stopwords
                word not in string.punctuation):  # remove punctuation
            # tweets_clean.append(word)
            stem_word = stemmer.stem(word)  # stemming word
            tweets_clean.append(stem_word)
    return tweets_clean

def bag_of_words(tweet):
    words = clean_tweets(tweet)
    words_dictionary = dict([word, True] for word in words)
    return words_dictionary


# test des données nltk
# positive tweets feature set
pos_tweets_set = []
for tweet in pos_tweets:
    pos_tweets_set.append((bag_of_words(tweet), 'positive'))

# negative tweets feature set
neg_tweets_set = []
for tweet in neg_tweets:
    neg_tweets_set.append((bag_of_words(tweet), 'negative'))

from random import shuffle

shuffle(pos_tweets_set)
shuffle(neg_tweets_set)


test_set = pos_tweets_set[:3000] + neg_tweets_set[:3000]
train_set = pos_tweets_set[3000:] + neg_tweets_set[3000:]

classifier = NaiveBayesClassifier.train(train_set)

accuracy = classify.accuracy(classifier, test_set)


with open('Sentiment_Analysis_polarity.txt', 'w') as csvfile:
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
            print(tweet)
            custom_tweet_set = bag_of_words(tweet)
            # probability result
            prob_result = classifier.prob_classify(custom_tweet_set)



            with open('Sentiment_Analysis_polarity.txt', 'a') as csvfile:

                  csvfile.writelines({

                      prob_result.max() + " " + data
                })


        except Exception as e:
            pass

