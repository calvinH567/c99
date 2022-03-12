import os
import shutil
source = input("Enter Source: ")
destination = input("Enter Destination: ")
source=source+'/'
destination=destination+'/'
listOfFiles=os.listdir(source)
for file in listOfFiles:
    shutil.move((source,destination),file)