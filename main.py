import pyttsx3
import platform
import obd
import time


def speechFunction (text): 
    try:
       engine = pyttsx3.init()
       engine.say(text)
       engine.runAndWait()
       engine.stop()
    except:
        print("speech failed")


simMode = platform.system() == 'Windows';


if(simMode):
    speechFunction("Windows.") #debug statement
    #windows 'mode' is essentially a simulated test case rather than live use.
else:
    speechFunction("Active. Initiating Connection")
    connection = obd.OBD()
    #linux 'mode' assumed live use.
    if(connection.is_connected()):
        speechFunction("Connection successful.")

i = 0

while(True):
    
    if(i % 60 == 0):
        print("temp")
        speechFunction("Temp Check")
        
    
    if(i % 10 == 0):
        print("speed")
        speechFunction("Speed Check")
    
    time.sleep(1)
    i += 1
