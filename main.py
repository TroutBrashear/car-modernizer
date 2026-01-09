import pyttsx3
import platform
import obd
import time


simMode = platform.system() == 'Windows'
connection = null


def speechFunction (text): 
    try:
       engine = pyttsx3.init()
       engine.say(text)
       engine.runAndWait()
       engine.stop()
    except:
        print("speech failed")
        

def speedCheck():
    if(simMode):
        speechFunction("Speed Check")
    else:
        response = str(connection.query(obd.commands.SPEED))
        speechFunction(response)

def tempCheck():
    if(simMod):
        speechFunction("Temp Check")
    else:
        response = str(connection.query(obd.commands.OIL_TEMP))
        speechFunction(response)

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
        tempCheck()
            
        
    
    if(i % 10 == 0):
        print("speed")
        speedCheck()
            
    
    time.sleep(1)
    i += 1
