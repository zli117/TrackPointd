# TrackPointd
systemd service for setting up Thinkpad trackpoint automatically

 - Install: `sudo python3 setup.py install`
 - To customize speed, sensitivity, and drift time: Modify `/etc/trackpointd.conf`
 - Start the service:

 ```bash
 sudo systemctl start trackpointd
 ```

 - Enable the server to start automatically on boot:

 ```bash
 sudo systemctl enable trackpointd
 ```
