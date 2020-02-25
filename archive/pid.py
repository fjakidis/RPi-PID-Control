from pid_library import *

### PIN CONFIGURATIONS

# Setup wiringpi
wp.wiringPiSetupGpio()

# Setup inputs (hall sensors and motor encoders)
wp.pinMode(HALL_11,INPUT)
wp.pinMode(HALL_12,INPUT)
wp.pinMode(HALL_13,INPUT)


wp.pinMode(HALL_14,INPUT)
wp.pinMode(HALL_15,INPUT)
wp.pinMode(HALL_16,INPUT)

wp.pinMode(ENCODER_1,INPUT)
wp.pinMode(ENCODER_2,INPUT)

# Setup outputs
wp.pinMode(OUTPUT_1,OUTPUT)
wp.pinMode(OUTPUT_2,OUTPUT)

### 

x = read(PIN)
print('{}\n'.format(x))

time.sleep(0.1)

wp.digitalWrite(PIN,1)

x = read(PIN)
print('{}\n'.format(x))


###




# Plot Signals


# PID Calculation Functions

