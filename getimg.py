import glob,os
import sys,shutil
import requests
import string,random


api_key=input("Enter the API --: ")

# api_key ="ocrGpnMuKrJ6RUEZKcEj3Jrq"  #change api key 

root_dir=sys.path[0]


path=root_dir+'\img\\*' #change input image path if needed


ext_allow=['jpg','png','jpeg']
dest=root_dir+'\\checks'
out_path=root_dir+'\\outputs\\'

#making DIR
os.mkdir(dest)

# move first 40 to the folder
cont=glob.glob(path)
if len(cont) >= 45: 
    n=45
else:
    n=len(cont)



for i in range(0,n):  #change upper range to =< 49
    ext=cont[i].split('.')
    if ext[-1].lower() in ext_allow:
        name=cont[i].split('\\')
        destn=dest+'\\'+name[-1]
        shutil.move(cont[i],destn)


#removing background

image=glob.glob(dest+'\\*')  
for img in image:
    
    response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(img, 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': api_key},
        )
    name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if response.status_code == requests.codes.ok:
        with open(out_path+name+'.png', 'wb') as out:
            out.write(response.content)
        print('saved --> '+name+'.png')


# removing Dir
shutil.rmtree(dest) 
# os.rmdir(dest)

