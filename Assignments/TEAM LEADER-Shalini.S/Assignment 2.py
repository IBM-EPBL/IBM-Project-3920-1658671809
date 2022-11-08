# Temperature - Humidity

import sys
import math

print('Celsius       Fahrenheit       Humidity')
dp = 0
c = 0
ind= ""
def frost_point(c,dpc):
    dpk = 273.15 + dpc
    tak = 273.15 + c
    fpk = dpk - tak + 2671.02 / ((2954.61 / tak) + 2.193665 * math.log(tak) - 13.3448 )
    return fpk - 273.15

def dew_point(c,rh):
    A = 17.27
    B = 273.7
    
    alpha = ((A*c) / (B+c)) + math.log(rh/100.0)
    dp = (B * alpha) / (A - alpha)
    
for c in range(30,71,1):
    f = int((c * 1.8) + 32)
    hum = 100 * ((math.e**((17.625*dp)/(243.04 + dp))) / (math.e**((17.625 * f)/(243.04 + f))))
    humidity = 100 * hum
    
    if f >= 100:
        ind = '!!!!  Over Heated  !!!!'
        print('Warning : ',ind)
        print('''
              ''')
              
    else:
        print('')

    print(c,'       ',f,'       %.2f' %humidity)