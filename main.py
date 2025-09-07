#main
import pandas as pd
df = pd.read_csv('results.csv') 
from scripts.average_wpm import average_wpm
from scripts.avg_acc import avg_acc
from scripts.consistency import consistency
average_wpm(df)
avg_acc(df)
consistency(df)

