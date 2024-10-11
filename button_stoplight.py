#Importing GPIO and time libraries so the code can work with the GPIO 
# pins and have the light turn on for certain amounts of time
import RPi.GPIO as GPIO
import time
#Tells the program which naming conventions to use for the GPIO pins
GPIO.setmode(GPIO.BCM)

#Setup the s pin
GPIO.setup(6,GPIO.IN)


#Creates variable to store the number of the GPIO pin needed
num = 0

while num == 0:
	if GPIO.input(6) == True:
		#Green LED for 5 seconds
		#Assigns the variable the value of the number for the GPIO pin 
		# needed to turn on the correct LED
		num = 17
		GPIO.setwarnings(False)
		#Tells the program to use the GPIO pin as output
		GPIO.setup(num,GPIO.OUT)
		#Prints text in the teriminal that tells the user the LED is on
		print("Green LED on")
		#Sends power to the GPIO pin, turning the LED on
		GPIO.output(num,GPIO.HIGH)
		#Pauses the program for a certain amount of time
		time.sleep(5)
		#Prints text in the teriminal that tells the user the LED is off
		print("Green LED off")
		#Stops sending power to the GPIO pin, turning the LED off
		GPIO.output(num,GPIO.LOW)


		#Blue LED for 1 second
		#Assigns the variable the value of the number for the GPIO pin 
		# needed to turn on the correct LED
		num = 19
		GPIO.setwarnings(False)
		#Tells the program to use the GPIO pin as output
		GPIO.setup(num,GPIO.OUT)
		#Prints text in the teriminal that tells the user the LED is on
		print("Blue LED on")
		#Sends power to the GPIO pin, turning the LED on
		GPIO.output(num,GPIO.HIGH)
		#Pauses the program for a certain amount of time
		time.sleep(1)
		#Prints text in the teriminal that tells the user the LED is off
		print("Blue LED off")
		#Stops sending power to the GPIO pin, turning the LED off
		GPIO.output(num,GPIO.LOW)


		#Red LED for 4 seconds
		#Assigns the variable the value of the number for the GPIO pin 
		# needed to turn on the correct LED
		num = 18
		GPIO.setwarnings(False)
		#Tells the program to use the GPIO pin as output
		GPIO.setup(num,GPIO.OUT)
		#Prints text in the teriminal that tells the user the LED is on
		print("Red LED on")
		#Sends power to the GPIO pin, turning the LED on
		GPIO.output(num,GPIO.HIGH)
		#Pauses the program for a certain amount of time
		time.sleep(4)
		#Prints text in the teriminal that tells the user the LED is off
		print("Red LED off")
		#Stops sending power to the GPIO pin, turning the LED off
		GPIO.output(num,GPIO.LOW)
