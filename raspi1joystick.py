import Rpi.Gpio as Gpio
from time import sleep
import pygame

pygame.init()
pygame.joystick.init()
joystick=pygame.joystick.Joystick(0)

#setup the gpio pins
Gpio.setmode(Gpio.borad)
#Gpio.setmode(Gpio.BCM)
Gpio.setwarnings(False)

#declare  the pins off frist  motors
motorA1=2
motorA2=3

#declare  the pins offsecond  motors
motorB1=5
motorB2=6

#declare  the pins offthrid motors
motorC1=7
motorC2=8

#declare  the pins off four  motors
motorD1=9
motorD2=10

#declare  the pins off fifth  motors
motorE1=11
motorE2=12

#declare  the pins off Sixthly  motors
motorF1=13
motorF2=14

#declare  the pins off VII  motors
motorG1=15
motorG2=16

#declare  the pins off Eighth  motors
motorZ1=17
motorZ2=18


#set the pins as output
Gpio.setup(motorA1,Gpio.OUT)
Gpio.setup(motorA2,Gpio.OUT)

Gpio.setup(motorB1,Gpio.OUT)
Gpio.setup(motorB1,Gpio.OUT)

Gpio.setup(motorC1,Gpio.OUT)
Gpio.setup(motorC1,Gpio.OUT)

Gpio.setup(motorD1,Gpio.OUT)
Gpio.setup(motorD1,Gpio.OUT)

Gpio.setup(motorE1,Gpio.OUT)
Gpio.setup(motorE2,Gpio.OUT)

Gpio.setup(motorF1,Gpio.OUT)
Gpio.setup(motorF2,Gpio.OUT)

Gpio.setup(motorG1,Gpio.OUT)
Gpio.setup(motorG2,Gpio.OUT)

Gpio.setup(motorZ1,Gpio.OUT)
Gpio.setup(motorZ2,Gpio.OUT)

#set the pwm pins
# We have set our PWM frequency to 500.
R1=Gpio.PWM(motorA1,500)
R2=Gpio.PWM(motorA2,500)

R3=Gpio.PWM(motorB1,500)
R4=Gpio.PWM(motorB2,500)

R5=Gpio.PWM(motorC1,500)
R6=Gpio.PWM(motorC2,500)

R7=Gpio.PWM(motorD1,500)
R8=Gpio.PWM(motorD2,500)

R9=Gpio.PWM(motorE1,500)
R10=Gpio.PWM(motorE2,500)

R11=Gpio.PWM(motorF1,500)
R12=Gpio.PWM(motorF2,500)

R13=Gpio.PWM(motorG1,500)
R14=Gpio.PWM(motorG2,500)

R15=Gpio.PWM(motorZ1,500)
R16=Gpio.PWM(motorZ2,500)

R1.start(0)
R2.start(0)
R3.start(0)
R4.start(0)
R5.start(0)
R6.start(0)
R7.start(0)
R8.start(0)
R10.start(0)
R11.start(0)
R12.start(0)
R13.start(0)
R14.start(0)
R15.start(0)
R16.start(0)

#The main code
while True:
   pygame.event.pump()
   Yvert=joystick.get_axis(1)
   Xhorz=joystick.get_axis(0)
   Yvert1=joystick.get_axis(2)
#HHorizontally mounted motors that move Motors counterclockwise forward
   if Yvert<0:
    print('Forward')

    Gpio.output(motorA1,Gpio.LOW)
    for i in range(0,101,1):
      R2.ChangeDutyCycle(.85*i) #provide duty cycle in the range 0-100

    Gpio.output(motorB1,Gpio.LOW)
    for i in range(0,101,1):
      R4.ChangeDutyCycle(.85*i) 

    Gpio.output(motorC1,Gpio.LOW)
    for i in range(0,101,1):
      R6.ChangeDutyCycle(.85*i) 
    
    Gpio.output(motorD1,Gpio.LOW)
    for i in range(0,101,1):
      R8.ChangeDutyCycle(.85*i) 

   elif Yvert<0:
    print('backward')
    
    Gpio.output(motorA2,Gpio.LOW)
    for i in range(0,101,1):
      R1.ChangeDutyCycle(.85*i) #provide duty cycle in the range 0-100

    Gpio.output(motorB2,Gpio.LOW)
    for i in range(0,101,1):
      R3.ChangeDutyCycle(.85*i) 

    Gpio.output(motorC2,Gpio.LOW)
    for i in range(0,101,1):
      R5.ChangeDutyCycle(.85*i) 
    
    Gpio.output(motorD2,Gpio.LOW)
    for i in range(0,101,1):
      R7.ChangeDutyCycle(.85*i) 

#vertically mounted motors that move motors counterclockwise forward
   elif Yvert1<0:
    print('up')
    
    Gpio.output(motorE1,Gpio.LOW)
    for i in range(0,101,1):
      R10.ChangeDutyCycle(.85*i) #provide duty cycle in the range 0-100

    Gpio.output(motorF1,Gpio.LOW)
    for i in range(0,101,1):
      R12.ChangeDutyCycle(.85*i) 

    Gpio.output(motorG1,Gpio.LOW)
    for i in range(0,101,1):
      R14.ChangeDutyCycle(.85*i) 
    
    Gpio.output(motorZ1,Gpio.LOW)
    for i in range(0,101,1):
      R16.ChangeDutyCycle(.85*i) 
    #vertically mounted motors that move motors clockwise Down 
   elif Yvert1>0 :
    print('Down')
    
    Gpio.output(motorE2,Gpio.LOW)
    for i in range(0,101,1):
      R9.ChangeDutyCycle(.85*i) 

    Gpio.output(motorF2,Gpio.LOW)
    for i in range(0,101,1):
      R11.ChangeDutyCycle(.85*i) 

    Gpio.output(motorG2,Gpio.LOW)
    for i in range(0,101,1):
      R13.ChangeDutyCycle(.85*i) 
    
    Gpio.output(motorZ2,Gpio.LOW)
    for i in range(0,101,1):
      R15.ChangeDutyCycle(.85*i) 
    
    #Motors installed horizontally and in a right direction
   elif Xhorz>0 :
    print('right')
    Gpio.output(motorA1,Gpio.LOW)
    for i in range(0,101,1):
      R2.ChangeDutyCycle(.85*i) #provide duty cycle in the range 0-100

    Gpio.output(motorB1,Gpio.LOW)
    for i in range(0,101,1):
      R4.ChangeDutyCycle(.85*i) 
    
    Gpio.output(motorC2,Gpio.LOW)
    for i in range(0,101,1):
      R5.ChangeDutyCycle(.85*i) 
    
    Gpio.output(motorD2,Gpio.LOW)
    for i in range(0,101,1):
      R7.ChangeDutyCycle(.85*i)

     #Motors installed horizontally and in a Lfet direction
   elif Xhorz<0 :
    print('LEFT')
    
    Gpio.output(motorA2,Gpio.LOW)
    for i in range(0,101,1):
      R1.ChangeDutyCycle(.85*i) 

    Gpio.output(motorB2,Gpio.LOW)
    for i in range(0,101,1):
      R3.ChangeDutyCycle(.85*i) 
    
    
    Gpio.output(motorC1,Gpio.LOW)
    for i in range(0,101,1):
      R6.ChangeDutyCycle(.85*i) 
    
    Gpio.output(motorD1,Gpio.LOW)
    for i in range(0,101,1):
      R8.ChangeDutyCycle(.85*i)          
#Stop motors
   else:
    print('stop')
    Gpio.output(motorA1,Gpio.LOW)
    Gpio.output(motorA2,Gpio.LOW)
    Gpio.output(motorB1,Gpio.LOW)
    Gpio.output(motorB2,Gpio.LOW)   
    Gpio.output(motorC1,Gpio.LOW)
    Gpio.output(motorC2,Gpio.LOW) 
    Gpio.output(motorD1,Gpio.LOW)
    Gpio.output(motorD2,Gpio.LOW)
    Gpio.output(motorE1,Gpio.LOW)
    Gpio.output(motorE2,Gpio.LOW)
    Gpio.output(motorF1,Gpio.LOW)
    Gpio.output(motorF2,Gpio.LOW)
    Gpio.output(motorG1,Gpio.LOW)
    Gpio.output(motorG2,Gpio.LOW)
    Gpio.output(motorZ1,Gpio.LOW)
    Gpio.output(motorZ2,Gpio.LOW)
     
   sleep(0.3)
Gpio.cleanup()

    
    
    

    





    

    

   
 

    
    

    
    
    

    



