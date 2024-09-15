# sh-blinkstick
My blinkstick scripts.
These are my blinkstick scripts.

Based on examples [here](https://github.com/arvydas/blinkstick-python/wiki).

## Usage (to be checked...): 
create python venv 

```
python -m venv blinkstick
```

activate venv 

```
source blinkstick/bin/activate 
```

cd to venv 

```
cd blinkstick
```


clone repository 

```
git clone https://github.com/sampod/sh-blinkstick.git
```

install requirements 

```
pip install -r requirements.txt 
```

run 

```
python blinkstick/sh-blinstick/cpu-usage.py 
```

## Running as systemd service

For running as a service and autostarting refer to:
[this](https://github.com/torfsen/python-systemd-tutorial)
and
[this](https://www.unixsysadmin.com/systemd-user-services/).

Also if you want to use blinkstick from user serivice you'll need to add the udev-rule to allow that:
```
sudo blinkstick --add-udev-rule
```
or
```
echo "SUBSYSTEM==\"usb\", ATTR{idVendor}==\"20a0\", ATTR{idProduct}==\"41e5\", MODE:=\"0666\"" | sudo tee /etc/udev/rules.d/85-blinkstick.rules
```
[source](https://pypi.org/project/BlinkStick/)

Example systemd unit file: 

```
[Unit]
Description=sh-blinkstick service

[Service]
# Command to execute when the service is started
ExecStart=/home/user/blinkstick/bin/python /home/user/blinkstick/sh-blinkstick/cpu-usage.py
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=default.target
```

### Short howto:

Check your paths. 
Create file `~/.config/systemd/user/sh-blinkstick.service` 
If all goes well it should start with: 
```
systemctl --user start sh-blinkstick.service
```

For staring it at reboot:
```
systemctl --user enable sh-blinkstick.service
```
