#comparer resultat
import difflib
import matplotlib.pyplot as plt
pos = 0
neg =0
neut = 0
with open('Sentiment_Analysis_polarity_class_mots.txt', 'r') as ile:
    data = ile.readline()
    for data in ile:
        if data[0:8] == "positive":
            pos = pos + 1
        elif data[0:8] == "negative":
            neg = neg + 1
        else:
            neut = neut + 1

name = ["positifs" , "negatifs" , "neutres"]
explode = (0.15, 0.15, 0.15)
prob = [pos, neg, neut]
plt.pie(prob, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
plt.show()