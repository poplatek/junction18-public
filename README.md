Poplatek's public repository for Junction 2018
==============================================

In `examples` directory there are several examples for using different
Raspberry Pi modules and AWS services that may be useful in the challenge.

Pre-configured Raspberry Pis
----------------------------

For the challenge we can lend a few Raspberry Pis (3 Model B+) with a
reasonably fast 32GB SD card. They have Debian-based Raspbian 9 and a
selection of potentially useful libraries and utilities already installed.
The full lists of packages are found in `doc` directory.

* https://github.com/poplatek/junction18-public/blob/master/doc/installed_packages.txt - Installed Raspbian/Debian packages
* https://github.com/poplatek/junction18-public/blob/master/doc/installed_pip_packages.txt - Installed pip packages (for Python 2)
* https://github.com/poplatek/junction18-public/blob/master/doc/installed_pip3_packages.txt - Installed pip3 packages (for Python 3)

Incoming network connections are allowed only to port 22 (SSH), but this can be configured easily with `ufw`.

For most AWS tools to work the credentials (access key ID and secret access
key) have to be configured to `~/.aws/credentials`.
