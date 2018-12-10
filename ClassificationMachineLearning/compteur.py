

compt =0

with open('identifiants_identiques.txt', 'r') as file1:
    data = file1.readline()
    for data in file1 :
                if (data[0:8] == "negative"):
                    compt = compt+1

print(compt)

compt =0


with open('identifiants_identiques.txt', 'r') as file1:
    data = file1.readline()
    for data in file1 :
                if (data[0:8] == "positive"):
                    compt = compt+1

print(compt)


