with open('identifiants-identiques.txt', 'r') as ile:
    data = ile.readline()
    for data in ile:
        with open('Sentiment_Analysis_polarity_class_mots.txt', 'r') as file:
            dataT = file.readline()
            for dataT in file :
                    if (data[9:27] == dataT[9:27] and data[0:8] == dataT[0:8] and data[0:8] == "positive"):
                        with open('positif_identiques.txt', 'a') as file1:
                            file1.writelines({

                                data
                            })

with open('identifiants-identiques.txt', 'r') as ile:
    data = ile.readline()
    for data in ile:
        with open('Sentiment_Analysis_polarity_class_mots.txt', 'r') as file:
            dataT = file.readline()
            for dataT in file :
                    if (data[9:27] == dataT[9:27] and data[0:8] == dataT[0:8] and data[0:8] == "negative"):
                        with open('negatif_identiques.txt', 'a') as file1:
                            file1.writelines({

                                data
                            })

with open('identifiants-identiques.txt', 'r') as ile:
    data = ile.readline()
    for data in ile:
        with open('Sentiment_Analysis_polarity_class_mots.txt', 'r') as file:
            dataT = file.readline()
            for dataT in file :
                    if (data[8:26] == dataT[8:26] and data[0:7] == dataT[0:7]):
                        with open('neutrals_identiques.txt', 'a') as file1:
                            file1.writelines({

                                data
                            })


