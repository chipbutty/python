# evaluate golie statistics
import os
from pathlib import Path
import csv
##os.getcwd()
#os.path.dirname(os.path.abspath(__file__))

myPath = Path().absolute()
golieFile = os.path.join(myPath, r"\nhl-game-data\game_golie_stats.csv")

with open(golieFile) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        print(row)
