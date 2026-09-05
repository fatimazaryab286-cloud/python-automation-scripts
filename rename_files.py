import os
#ask user for folder
folder=input('give me the folder path:')
#get files from the folder
#loop through files

#get today's date
from datetime import date
today=date.today()
formatted_date=today.strftime('%Y-%m-%d')
#create the new filename
#rename the file
for filename in os.listdir(folder):
    os.rename(os.path.join(folder,filename), os.path.join(folder,formatted_date+'_'+filename))
print('your file is renamed succefully!')