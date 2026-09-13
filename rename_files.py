import os
#ask user for folder
folder=input('give me the folder path:')

#get today's date
from datetime import date
today=date.today()
formatted_date=today.strftime('%Y-%m-%d')

#rename the file
for filename in os.listdir(folder):
    os.rename(os.path.join(folder,filename), os.path.join(folder,formatted_date+'_'+filename))
print('your file is renamed succefully!')