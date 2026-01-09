import pyttsx3
import platform
import obd

engine = pyttsx3.init()

if(platform.system() == 'Windows'):
    engine.say("Windows.") #debug statement
    #windows 'mode' is essentially a simulated test case rather than live use.
elif(platform.system() == 'Linux'):
    engine.say("Active. Initiating Connection")
    engine.runAndWait()
    connection = obd.OBD()
    #linux 'mode' assumed live use.
    if(connectin.is_connected()):
        engine.say("Connection successful.")

engine.runAndWait()

