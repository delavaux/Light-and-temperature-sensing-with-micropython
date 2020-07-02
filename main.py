# main.py -- put your code here!

import machine
from machine import ADC
from machine import PWM
import time
import pycom

pycom.heartbeat(False)

pybytes.send_signal(2,1)

i = 0
avgtemp = 0
avgljus = 0
thresholdtemp = 22


pwm = PWM(0, frequency=50)
pwm_c = pwm.channel(0, pin='P12', duty_cycle=0.044)

adc = ADC(0)

bpin = adc.channel(pin='P14', attn = machine.ADC.ATTN_11DB)   # Light sensor
apin = adc.channel(pin='P13')   # temperature sensor

while True:


    val = apin.voltage()
    ljus = bpin.voltage()/0.0157                      # read an analog value

    temp=(val-500)/10

    avgtemp += temp
    avgljus += ljus

    time.sleep(6)

    i = i + 1

    if i == 10:
        avgtemp = avgtemp / 10
        avgljus = avgljus / 10

        print(avgljus)
        print(avgtemp)
        pybytes.send_signal(0,avgtemp)
        pybytes.send_signal(1,avgljus)

        avgtemp = 0
        avgljus = 0
        i = 0
