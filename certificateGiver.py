import pandas as pd
import sys
import random as rd
import datetime

if len(sys.argv) == 3:
    recentWeeksToIgnore = int(sys.argv[2])
    certificatesToGive = int(sys.argv[1])
    if certificatesToGive < recentWeeksToIgnore:
        print(
            "WARNING: IF THE NUMBER OF WEEKS TO IGNORE IS MORE THAN THE NUMBER OF CERTIFICATES TO GIVE THIS WILL "
            "EVENTUALLY CAUSE AN ERROR")
elif len(sys.argv) == 2:
    recentWeeksToIgnore = 3
    certificatesToGive = int(sys.argv[1])
    if certificatesToGive < recentWeeksToIgnore:
        print(
            "WARNING: IF THE NUMBER OF WEEKS TO IGNORE IS MORE THAN THE NUMBER OF CERTIFICATES TO GIVE THIS WILL "
            "EVENTUALLY CAUSE AN ERROR")
else:
    recentWeeksToIgnore = 3
    certificatesToGive = 5

df = pd.read_csv("classSpreadsheet.csv")

np_df = df.values

kidsDict = {}
kids = []

for i in range(0, df['Names'].size):
    kidsDict[i] = np_df[i]
    kids.append(i)

if recentWeeksToIgnore > len(kidsDict[0]) - 1:
    recentWeeksToIgnore = len(kidsDict[0]) - 1

if recentWeeksToIgnore > 0:
    for i in range(1, recentWeeksToIgnore + 1):
        for kid in reversed(kids):
            if kidsDict[kid][-i] == "CERTIFICATE":
                kids.remove(kid)

date = str(datetime.datetime.today().strftime('%d-%m-%Y'))
if date not in df.columns:
    df[date] = " "
else:
    overwriteToday = input("You have certificates already assigned for today. Are you sure you would like to "
                           "overwrite the certificates given today? (y/n)\n")
    if overwriteToday == 'y':
        df[date] = " "
        print("\nCERTIFICATES OVERWRITTEN\n")
    elif overwriteToday == 'n':
        print("Ok, no certificates have been given and no changes have been made to the certificate spreadsheet.")
        exit()
    else:
        overwriteToday = input("Sorry. I haven't understood your input. Please could you answer again, are you sure"
                               " you would like to overwrite the certificates given today? (y for yes/n for no)\n")
        if overwriteToday == 'y':
            df[date] = " "
            print("\nCERTIFICATES OVERWRITTEN\n")
        elif overwriteToday == 'n':
            print("Ok, no certificates have been given and no changes have been made to the certificate spreadsheet.")
            exit()
        else:
            overwriteToday = ("Sorry. I haven't understood your input. certificates have been given and no changes "
                              "have been made to the certificate spreadsheet. If you would still like to make changes "
                              "please run this program again")
            exit()

print("CERTIFICATES FOR: ")
for i in range(0, certificatesToGive):
    try:
        x = rd.randint(0, len(kids) - 1)
    except ValueError:
        print("ERROR: MOST LIKELY THERE ARE NO MORE CHILDREN YOU CAN GIVE CERTIFICATES TOO SINCE THE NUMBER OF "
              "WEEKS TO IGNORE IS TOO HIGH")
    kidForCertificate = kids.pop(x)
    df.loc[kidForCertificate, date] = "CERTIFICATE"
    print(format(kidsDict[kidForCertificate][0]))

df.to_csv("classSpreadsheet.csv", index=False)

print("SPREADSHEET HAS BEEN UPDATED")

