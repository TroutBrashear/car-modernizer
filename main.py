import pyttsx3
import platform
import obd
import time





engine = pyttsx3.init()
simMode = platform.system() == 'Windows';


if(simMode):
    engine.say("Windows.") #debug statement
    engine.runAndWait()
    #windows 'mode' is essentially a simulated test case rather than live use.
else:
    engine.say("Active. Initiating Connection")
    engine.runAndWait()
    connection = obd.OBD()
    #linux 'mode' assumed live use.
    if(connection.is_connected()):
        engine.say("Connection successful.")
    engine.runAndWait()

i = 0

while(True):
    
    if(i % 60 == 0):
        print("temp")
        engine.say("Temp Check")
        engine.runAndWait()
        
    
    if(i % 10 == 0):
        print("speed")
        engine.say("Speed Check")
        engine.runAndWait()
    
    time.sleep(1)
    i += 1
