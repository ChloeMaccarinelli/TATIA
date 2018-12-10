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


def clean_text(phrase):
    # remove hyperlinks
    phrase = re.sub(r'https?:\/\/.*[\r\n]*', '', phrase)

    # remove hashtags
    # only removing the hash # sign from the word
    phrase = re.sub('#[\w\.\-]+', '', phrase)
    phrase = re.sub('@[\w\.\-]+', '', phrase)

    # tokenize tweets
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    phrase_tokens = tokenizer.tokenize(phrase)
    phrase_clean = []
    for word in phrase_tokens:
        if (word not in stopwords_english and  # remove stopwords
                word not in string.punctuation and
                word not in emoticons):
            stem_word = stemmer.stem(word)  # stemming word
            phrase_clean.append(stem_word)
    return phrase_clean

def bag_of_words(phrase):
    words = clean_text(phrase)
    words_dictionary = dict([word, True] for word in words)
    return words_dictionary


neutral = 0
pos =0
neg = 0
neut = 0

#datat = 640290626756476928

data = "A man displayed a gun during an argument with a group of mostly Somali-American teenagers at a McDonald’s in Minnesota after he wrongly suggested they were using welfare assistance to pay for their food, members of the group said. " \
       "The confrontation with the man, which was partly captured on a video that has been widely circulated on Twitter, occurred on Monday at a McDonald’s restaurant in Eden Prairie, Minn., a suburb southwest of Minneapolis, and ended without any shots fired or injuries sustained." \
       "On Wednesday, the Eden Prairie police arrested Lloyd Edward Johnson, 55, under probable cause for second-degree assault, the city said in a statement. Mr. Johnson was being held at the Hennepin County Adult Detention Center. Joyce Lorenz, a spokeswoman for the city, said on Thursday that the Hennepin County attorney would decide whether to file any charges."
words = clean_text(data)


#tweets = api.get_status(datat)
#tweet = tweets.text
#print("tweet de base => " + tweet)


words = clean_text(data)
print(words)
listeNeg = []
with open('negativeWords.txt','r') as n :
    neg = n.readline()
    for word in words:
        for neg in n :
            if word[0:] in neg :
                listeNeg.append(word)

print('nombre mots negatifs')
print(listeNeg.__len__())
print (listeNeg)

listePos=[]
with open('positiveWords.txt','r') as n :
    pos = n.readline()
    for word in words:
        for pos in n :
            if word[0:] in pos :
                listePos.append(word)
print('nombre mots positifs')
print(listePos.__len__())
print(listePos)
if listeNeg.__len__() == listePos.__len__() :
    neutral = 1
    print('phrase neutre')
#print(neutral)

words.clear()

classify = "neutral"
if listeNeg.__len__() < listePos.__len__():
    classify = "positive"
    print('phrase positive')
elif listeNeg.__len__() > listePos.__len__():
    print('phrase negative')
    classify ="negative"

with open('Sentiment_Analysis_polarity.txt', 'a') as csvfile:

    csvfile.writelines({

        classify + " " +data
    })





