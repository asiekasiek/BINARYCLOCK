#!/usr/bin/env python3

from datetime import time
from datetime import datetime
import time
import os
try:
    while True:								#loop, if you want to stop: ctrl+C
        t = datetime.time(datetime.now())	#current time
        tstr = str(t)						#change for string
        thour = bin(int(tstr[0:2]))			#current hour in binary system
        tmin = bin(int(tstr[3:5]))			#current minute in binary system
        tsec = bin(int(tstr[6:8]))			#current second in binary system
        print("Czas binarny: " + thour[2:] + ":" + tmin[2:] + ":" + tsec[2:])	#print binary time
        time.sleep(1)
        os.system("clear")
except:
    print("Do zobaczenia")
