from distutils.core import setup

setup(
    name='trackpointd',
    version='1.0',
    description='Daemon for setting the track point',
    data_files=[('/lib/systemd/system/', ['trackpointd.service']),
                ('/usr/bin/', ['trackpointd.py']),
                ('/etc/', ['trackpointd.conf'])]
)
