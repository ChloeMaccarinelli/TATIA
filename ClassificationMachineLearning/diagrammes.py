#comparer resultat
import difflib
import matplotlib.pyplot as plt
import ClassificationMachineLearning.classification_ml.py

from ClassificationMachineLearning.classification_ml import classifier, test_set

pos = 0
neg =0



accuracy = ClassificationMachineLearning.classification_ml.classify.accuracy(classifier, test_set)
print(accuracy)
plt.bar(accuracy)
#with open('identifiants_identiques.txt', 'r') as ile:
#    data = ile.readline()
#   for data in ile:
#       if data[0:8] == "positive":
#           pos = pos + 1
 #       elif data[0:8] == "negative":
#          neg = neg + 1


#name = ["positifs" , "negatifs"]
#explode = (0.15, 0.15)
#prob = [pos, neg]
#plt.pie(prob, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
#plt.show()