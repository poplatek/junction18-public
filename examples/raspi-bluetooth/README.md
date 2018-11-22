## Bluetooth Examples

Raspberry Pi 3 Model B+ has built-in Bluetooth 4.2 with BLE (Bluetooth Low
Enery) support.

In this directory there are a some public github repositories checkt out as an
example of how to use Bluetooth. Use with e.g. an Android beacon software to
experiment.

* https://github.com/pybluez/pybluez.git

Python Bluetooth library PyBluez, which is not currently actively supported so
there may be problems. There are multiple examples in `examples` directory for
using simple Bluetooth or BLE. BLE support of PyBluez is experimental, so it
may be glitchy or unreliable. BLE Beacon seems to work better than Beacon
scanner.

* https://github.com/taka-wang/py-beacon.git

Basic beacon scanner, which just prints all the beacons it hears, with their
data and signal strength. Run with `sudo python test.py`.

* https://github.com/ashokgelal/iBeacon-Scanner.git

Includes a rudimentary and probably quite inaccurate attempt to calculate
distance to the beacons. Run with `sudo python scanner.py`, and use wide
terminal window for readable output.
