import time
import sys
import ibmiotf.application
import ibmiotf.device
import random


#Provide your IBM Watson Device Credentials
organization = "jgvzno"
deviceType = "weather_device"
deviceId = "weather_today"
authMethod = "token"
authToken = "TSjEJjU82tT(olJkdX"

# Initialize GPIO

temperature=random.randint(0,100)
humidity=random.randint(0,100)
pressure=random.randint(0,100)
enthalpy=17
power=18


def myCommandCallback(cmd):
    print("Command received: %s" % cmd.data['command'])
    print(cmd)
        


try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        #Get Sensor Data from DHT11
        

        temperature=random.randint(0,100)
        humidity=random.randint(0,100)
        pressure=random.randint(0,100)
        enthalpy=17
        power=18
        data = {"d":{ 'temperature' : temperature, 'humidity': humidity ,'pressure': pressure,'enthalpy' : enthalpy,'power' : power}}
        #print data
        def myOnPublishCallback():
            print ("Published Temperature = %s C" % temperature, "Humidity = %s %%" % humidity, "to IBM Watson")

        success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(1)
        
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
