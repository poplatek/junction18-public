#basic setup
from sense_hat import SenseHat
sense = SenseHat()
#This makes the HAT align to upside down orientation 
#(with RasPi HDMI port facing up)
sense.set_rotation(180)
#Show message
sense.show_message(
	"Poplatek",
	scroll_speed=0.05,
	text_colour=[20,250,20],
	back_colour=[0,50,50])
#logo
sense.load_image('poplatek_logo_8.png')
#show the atmosphere metrics via console
temp = sense.get_temperature()
print("Temperature: %s C" % temp)
humidity = sense.get_humidity()
print("Humidity: %s %%rH" % humidity)
pressure = sense.get_pressure()
print("Pressure: %s Millibars" % pressure)
#show the accelometer metrics via console
north = sense.get_compass()
print("North: %s" % north)
gyro_only = sense.get_gyroscope()
print("gyro-p: {pitch}, gyro-r: {roll}, gyro-y: {yaw}".format(**gyro_only))
accel_only = sense.get_accelerometer()
print("accel-p: {pitch}, accel-r: {roll}, accel-y: {yaw}".format(**accel_only))