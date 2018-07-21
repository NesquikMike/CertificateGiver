import pandas as pd
import sys
import random as rd

if len(sys.argv) == 3:
    recentWeeksToIgnore = int(sys.argv[2])
    certificatesToGive = int(sys.argv[1])
elif len(sys.argv) == 2:
    recentWeeksToIgnore = 3
    certificatesToGive = int(sys.argv[1])
else:
    recentWeeksToIgnore = 3
    certificatesToGive = 5

db = pd.read_csv("certificatesSpreadsheetTest.csv")

