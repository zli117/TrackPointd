# TrackPointd
Service for setting up Thinkpad trackpoint automatically

 - Install: `sudo python -m pip install .`
 - Modify `/etc/trackpointd.conf` to configure speed, sensitivity, and drift time
 - Start the service:

 ```bash
 sudo systemctl start trackpointd
 ```

 - Enable the service to start automatically on boot:

 ```bash
 sudo systemctl enable trackpointd
 ```

For newer Thinkpad models, the default path and attributes may not be correct. Use this instead:
```
# Configuration file for track point settings
# Location of the hardware settings
dir = /sys/devices/platform/i8042/serio1/
sensitivity = 220
```
