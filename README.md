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
[this](https://www.unixsysadmin.com/systemd-user-services/)

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
