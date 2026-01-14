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
if(simMode):
    import keyboard
    
    def summaryButtonPress():
        return keyboard.is_pressed('space')
else:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN)
    
    def summaryButtonPress():
        return GPIO.input(18)

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
        if(response.is_null()):
            speechFunction("no speed response")
            return
        speedValue = int(response.magnitude)
        speedLog.append(speedValue)
        if(speedValue > 80):
            speechFunction(str(response))

def tempCheck():
    if(simMode):
        simTemp = random.randint(85, 120)
        tempLog.append(simTemp)
        speechFunction(str(simTemp) + " degrees")
    else:
        response = connection.query(obd.commands.COOLANT_TEMP).value
        if(response.is_null()):
            speechFunction("no temp response")
            return
        tempValue = int(response.magnitude)
        tempLog.append(tempValue)
        if(tempValue > 105):
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
       
    if(summaryButtonPress()):
        print("summary")
        summarize()
    
    time.sleep(1)
    i += 1
