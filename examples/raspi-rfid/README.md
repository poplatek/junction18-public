RFID-RC522 usage instructions
=============================

GPIO pin setup
--------------
To make the RFID reader talk with your Raspberry Pi, you first need to 
use wires and (optionally) a breadboard to attach most of the pins on 
it to the Raspberry Pi GPIO interface pins.

The correct wiring from the RFID reader to the RasPi is as follows:

| RFID Pin Name | RasPi Pin# | RasPi Pin Name |
|---------------|------------|----------------|
| VCC           | 1          | 3V3            |
| RST           | 22         | GPIO25         |
| GND           | Any GND    | Any GND        |
| MISO          | 21         | GPIO9          |
| MOSI          | 19         | GPIO10         |
| SCK           | 23         | GPIO11         |
| NSS           | 24         | GPIO8          |
| IRQ           | None       | None           |

The names of the connections on the RFID reader can be found at the root of their respective pins.

See the image below for a reference on the names of the pins on the Raspberry Pi, along with an example
recommended wiring layout for the RFID reader.

![GPIO pins](gpio-numbers-pi.png "GPIO pin layout for the Raspberry Pi 3+, with annotations showing an example wiring for the RFID reader")

You can find more information about GPIO pin layouts on the Raspberry Pi at https://www.raspberrypi.org/documentation/usage/gpio/

RFID tag writing and reading
----------------------------
Two small Python scripts have been written (or actually copied from https://pimylifeup.com/raspberry-pi-rfid-rc522/)
to demonstrate writing to an RFID tag and reading data from it.

Write.py can be used to read a user input string and then write it to an RFID tag which is presented to the RFID reader.
Read.py can then be used to read the information out of an RFID tag, and print out its tag ID and content.

More information about the MFRC522-RFID reader python library used by the two scripts can be found
at its git repository: https://github.com/mxgxw/MFRC522-python

More information
----------------
For longer instructions, see http://wiki.sunfounder.cc/index.php?title=How\_to\_Use\_an\_RFID\_RC522\_on\_Raspberry\_Pi
and https://pimylifeup.com/raspberry-pi-rfid-rc522/

Note that the first of these links shows an incorrect wiring layout for the RFID reader provided in the hackathon.
