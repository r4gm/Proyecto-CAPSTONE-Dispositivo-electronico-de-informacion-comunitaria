import max30102
import hrcalc

import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

client = mqtt.Client()
client.connect('broker.hivemq.com',1883,60)

while True:

    m = max30102.MAX30102()

    hr2 = 0
    sp2 = 0

    red, ir = m.read_sequential()
    
    hr,hrb,sp,spb = hrcalc.calc_hr_and_spo2(ir, red)

    print("hr detected:",hrb)
    print("sp detected:",spb)
    
    if(hrb == True and hr != -999):
        hr2 = int(hr)
        print("Heart Rate : ",hr2)
    if(spb == True and sp != -999):
        sp2 = int(sp)
        print("SPO2       : ",sp2)


    client.publish("Max30102G4GRG/heartrate", hr2)
    print("Ritmo Cardiaco " + str(hr2))
    client.publish("Max30102G4GRG/blood", sp2)
    print("Oxigeno en la Sangre " + str(sp2))

    time.sleep(1)

#client.disconnect()
