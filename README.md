Poplatek's public repository for Junction 2018
==============================================

In `examples` directory there are several examples for using different
Raspberry Pi modules and AWS services that may be useful in the challenge.

Pre-configured Raspberry Pis
----------------------------

For the challenge we can lend a Raspberry Pi (3 Model B+) with a
reasonably fast 32GB SD card. They have Debian-based Raspbian 9 and a
selection of potentially useful libraries and utilities already installed.
The full lists of packages are found in `doc` directory. Depending on the
amount of participating teams you might get more than one RasPi.

* [Installed Raspbian/Debian packages](doc/installed_packages.txt)
* [Installed pip packages for Python 2](doc/installed_pip_packages.txt)
* [Installed pip3 packages for Python 3](doc/installed_pip3_packages.txt)

Incoming network connections are allowed only to port 22 (SSH), but this can be configured easily with `ufw`.

For most AWS tools to work the credentials (access key ID and secret access
key) have to be configured to `~/.aws/credentials`.

(on-site update) Quickstart for our pre-configured Raspberry Pi
---------------------------------------------------------------

- WiFi is really bad now so it’s probably not usable. Also the WiFi information we got in advance has been changed. Wired ethernet should work as long as it gets a DHCP address.
- You can use monitor with HDMI and USB keyboard, or access RasPi over the net with SSH. They should answer to the address “poplahackXX.local” (look at the label) when you’re connected to the same network with the RasPi.
- Default username is ‘pi’ and you can get password from our people at our stand, or using Slack.
