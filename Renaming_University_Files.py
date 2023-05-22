import sys
import os
import shutil

cwd = os.getcwd()
Files = os.listdir(cwd)
Filename = Files[2]
Parts = Filename.split("_with")
Uni = Parts[1]
Str1 = Files[4] + Uni
Str2 = Files[6] + Uni

os.rename(Files[4],Str1)
os.rename(Files[6],Str2)

print("Done")
