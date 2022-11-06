import os
import shutil
 
source = "maestro-v2.0.0-midi"
destination = "midiFiles"
 
# gather all files
alldirs = os.listdir(source)

# iterate on all files to move them to destination folder
for dir in alldirs:
    dirSourcePath = f"{source}/{dir}"
    yearFiles = os.listdir(f"{source}/{dir}")  # specific folder
    for file in yearFiles:
        shutil.move(f"{dirSourcePath}/{file}", f"{destination}/{file}")
    

