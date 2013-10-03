import serial
from time import sleep

vasak = serial.Serial('/dev/ttyACM0')
parem = serial.Serial('/dev/ttyACM1')

def jookse(kiirus):
    vasak.write('sd'+str(kiirus)+'\n')
    parem.write('sd-'+str(kiirus)+'\n')

def tagane(kiirus):
    vasak.write('sd-'+str(kiirus)+'\n')
    parem.write('sd'+str(kiirus)+'\n')

def ymberpoord():
    vasak.write('sd20\n')
    parem.write('sd20\n')
    
def seis():
    vasak.write('sd20\n')
    parem.write('sd20\n')    
##
##while (True):
##    jookse(20)
##    sleep(1.5)
##    ymberpoord()

    
