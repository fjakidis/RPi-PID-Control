import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setMode(23, OUTPUT);
GPIO.setMode(24, OUTPUT);
GPIO.setMode(25, OUTPUT);
GPIO.setMode(16, OUTPUT);

// Setup input 
GPIO.setMode(17, INPUT);
GPIO.setMode(27, INPUT);
GPIO.setMode(22, INPUT)