compt =0

with open('identifiants-identiques.txt', 'r') as file1:
    data = file1.readline()
    for data in file1 :
        with open('Sentiment_Analysis_polarity_class_mots.txt', 'r') as file:
            dataT = file.readline()
            for dataT in file :
                if (dataT[9:27] == data[8:26] and dataT[0:7] == "neutral" and dataT[0:8] == "negative"):
                    compt = compt+1

print(compt)

compt =0

with open('identifiants-identiques.txt', 'r') as file1:
    data = file1.readline()
    for data in file1 :
                if (data[0:7] == "neutral"):
                    compt = compt+1

print(compt)



