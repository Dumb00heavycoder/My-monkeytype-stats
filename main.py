#main
import pandas as pd
df = pd.read_csv('results.csv') 
from scripts.average_wpm import average_wpm
from scripts.avg_acc import avg_acc

average_wpm(df)
avg_acc(df)
