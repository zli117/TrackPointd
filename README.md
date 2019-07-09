# TrackPointd
Service for setting up Thinkpad trackpoint automatically

 - Install: `sudo python3 setup.py install`
 - Modify `/etc/trackpointd.conf` to configure speed, sensitivity, and drift time
 - Start the service:

 ```bash
 sudo systemctl start trackpointd
 ```

 - Enable the service to start automatically on boot:

 ```bash
 sudo systemctl enable trackpointd
 ```
