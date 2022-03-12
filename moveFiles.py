import os
import shutil
i = input("Enter Source: ")
o = input ("ENter destination: ")
i=i+'/'
o=o+'/'
listOfFiles= os.listdir(i)
for file in listOfFiles:
    shutil.move((i+file),o)