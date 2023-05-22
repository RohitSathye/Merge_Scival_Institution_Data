import os
import csv
import pandas as pd
import glob

cwd = os.getcwd()
Iterables = glob.glob('*.{}'.format('csv'))
Newfile = "HBCU_Publications_by_Subject_Area.csv"
Merged_collaboration_HBCU = pd.DataFrame()

Merged_collaboration_HBCU = pd.concat([pd.read_csv(file) for file in Iterables ], ignore_index=True)

Merged_collaboration_HBCU.to_csv(Newfile,index=False,encoding='utf8')
print("Done")
    
          
            



