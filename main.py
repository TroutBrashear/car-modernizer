import pyttsx3
import platform
import obd
import time
import random


#var defs
simMode = platform.system() == 'Windows'
connection = None

speedLog = []
tempLog = []


#function defs
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
        simSpeed = random.randint(40, 70)
        speedLog.append(simSpeed)
        speechFunction(str(simSpeed) + " mph")
    else:
        response = connection.query(obd.commands.SPEED).value.to('mph')
        speedLog.append(int(response.magnitude))
        speechFunction(str(response))

def tempCheck():
    if(simMode):
        simTemp = random.randint(85, 120)
        tempLog.append(simTemp)
        speechFunction(str(simTemp) + " degrees")
    else:
        response = connection.query(obd.commands.COOLANT_TEMP).value
        tempLog.append(int(response.magnitude))
        speechFunction(str(response))

def summarize():
    readout = "Trip Summary: "
    #average out speed
    if(len(speedLog) > 0):
        averageSpeed = sum(speedLog) / len(speedLog)
        readout += f"Speed average is {averageSpeed}"
        
    #average out coolant temp
    if(len(tempLog) > 0):
        averageTemp = sum(tempLog) / len(tempLog)
        readout += f"Temperature average is {averageTemp}"
    #speech
    speechFunction(readout)



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
    
    if(i % 10 == 0):
        print("temp")
        tempCheck()
            
        
    
    if(i % 5 == 0):
        print("speed")
        speedCheck()
       
    #todo: tie this to user request (button) rather than time
    if(i % 20 == 0):
        print("summary")
        summarize()
            
    
    time.sleep(1)
    i += 1
