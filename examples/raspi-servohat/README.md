# Adafruit Servo Bonnet

The Servo bonnet can be used to connect one or more servo motors to the Raspberry Pi. Servos can be used to prototype things like doors, product dispensers, gates, etc.

Check out a hilarious example from: https://www.instagram.com/p/BqJnlXeBhtG/ 

PS. We also have some servos which can be directly connected with the Grove shield. Those *can* be used with but don't need the Servo Bonnet.

## Connecting the Servo Bonnet to Raspberry Pi 3

Since the RasPi 3 B+ has PoE pins, and the Servo Bonnet has a small connector, the Bonnet *cannot* be directly placed on top of the RasPi. It might cause a short circuit. 

You either need to use a raiser, put another shield like the GrovePi shield in between, or simply connect it using jumper wires to the Pi. For using jumper wires keep in mind the Servo Bonnet is connected using I2C, so you only need a few wires.

The Servo Bonnet also needs an external power supply.

## Adafruit's instructions for the Servo Hat

https://github.com/adafruit/Adafruit_Python_PCA9685

## Controlling the servos

Check out example from:
https://github.com/adafruit/Adafruit_Python_PCA9685/tree/master/examples

## Quirks

The servo will immediately move to the position you tell it to go to. You might need to move the servo in small increments to make it act less like an insane robot.

