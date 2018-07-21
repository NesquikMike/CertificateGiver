import pandas as pd
import sys
import random as rd
import datetime

if len(sys.argv) == 3:
    recentWeeksToIgnore = int(sys.argv[2])
    certificatesToGive = int(sys.argv[1])
elif len(sys.argv) == 2:
    recentWeeksToIgnore = 3
    certificatesToGive = int(sys.argv[1])
else:
    recentWeeksToIgnore = 3
    certificatesToGive = 5

df = pd.read_csv("classSpreadsheet.csv")

print(df.head(5))

np_df = df.values

kidsDict = {}
kids = []

print(df['Names'].size)
for i in range(0, df['Names'].size):
    kidsDict[i] = np_df[i]
    kids.append(i)

if recentWeeksToIgnore > len(kidsDict[0]) - 1:
    recentWeeksToIgnore = len(kidsDict[0]) - 1

if recentWeeksToIgnore > 0:
    for i in range(1, recentWeeksToIgnore):
        for kid in kids:
            if kidsDict[kid][-i] == "CERTIFICATE":
                kids.remove(kid)

date = str(datetime.datetime.today().strftime('%d-%m-%Y_%H_%M_%S'))
df[date] = " "

print("CERTIFICATES FOR: ")
for i in range(0, certificatesToGive):
    x = rd.randint(0, len(kids) - 1)
    kidForCertificate = kids.pop(x)
    df.loc[kidForCertificate, date] = "CERTIFICATE"
    print(format(kidsDict[kidForCertificate][0]))

df.to_csv("classSpreadsheet.csv", index=False)

print("SPREADSHEET HAS BEEN UPDATED")

