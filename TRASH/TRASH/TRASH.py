import RPi.GPIO as GPIO 
import time 
GPIO.setmode(GPIO.BCM)

#variables for tri and echo pins 
# TODO: This needs to be initiated as a constructor.
TRIG = 23
ECHO = 24



print "Distance Measurment In Progress"

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)

print "Waiting for Sensor To Settle"
time.sleep(2)

# This is the code that needs to run
# TODO: This needs to be written in a function 

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO) ==0:
    pulse_start = time.time()

while GPIO.input(ECHO) ==1:
    pulse_end = time.time()

pulse_duration = pulse_end - pulse_start 

distance = pulse_duration * 17150

distance = round(distance, 2)

print "Distance:", distance, "cm"

GPIO.cleanup()

class Ultrasonic_sensor:  
    ## This is the class for the sensor
    def __init__(self,T, E):
        TRIG = T
        ECHO = E

        print "Initializing the pins"
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)

        GPIO.output(TRIG, False)
        
        return 0
    
     def setup(self):
        GPIO.output(TRIG, False)
        time.sleep(2)
        print "setup complete"
        return 0

    def pulse(self):
        # Now we pulse the signal 
        GPIO.output(TRIG, True)
        time.sleep(0.0001)
        GPIO.output(TRIG, False)
        
        # Listen to the echo pin
        while GPIO.input(echo) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()
        
        pulse_duration = pulse_start - pulse.end

        # distance calculation:

        distance =  pulse_duration * 17150

        distance = round(distance, 2)

        return 0 



# main  function:

sensor = Ultrasonic_sensor(23, 24)
sensor.setup
while true
    sensor.pulse()
    
    
