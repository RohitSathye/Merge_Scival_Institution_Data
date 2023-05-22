import os
import csv
import sys
import glob

cwd = os.getcwd()
Files = os.listdir(cwd)
Iterables  = glob.glob('*.{}'.format('csv'))
University = ""
Omit = '© 2023 Elsevier B.V. All rights reserved. SciVal, RELX Group and the RE symbol are trade marks of RELX Intellectual Properties SA, used under license.'

for file in Iterables:
    Temp = file.split("_Output.csv_")
    Newfile = "Modified_Authors_" + Temp[1]
    filename = open(file,"r",encoding='utf8')
    wrtfile = open(Newfile,"w",encoding='utf8',newline='')
    reader = csv.reader(filename)
    writer = csv.writer(wrtfile)
    line_count = 0

    for row in reader:
        line_count += 1
        if line_count == 2:
            University = row[1]
        if line_count == 13:
            row = row[:7]
            row.append('Institution')
            writer.writerow(row)
        if line_count > 13:
                if row:
                    if Omit not in row:
                        row = row[:7]
                        row.append(University)
                        writer.writerow(row)
            
    wrtfile.close()

print("Done")
    
          
            



