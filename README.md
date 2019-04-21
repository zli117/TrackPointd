# TrackPointd
systemd service for setting up Thinkpad trackpoint automatically

 - Modify [`trackpointd.conf`](trackpointd.conf) according to your preference
 - Modify [`trackpointd.service`](trackpointd.service) with your python install path in [`ExecStart`](https://github.com/Zonglin-Li6565/TrackPointd/blob/1def5f7017ec8919820378ff1c4c7cb551dada80/trackpointd.service#L6)
 - Then run `sudo python setup.py install` to install
 - Run `sudo systemctl start trackpointd` to start the daemon
 - Run `sudo systemctl enable trackpointd` for auto start
 - The config file will be installed to `/etc/`
