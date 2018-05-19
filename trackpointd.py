#!/usr/bin/python
"""
The daemon for automatically set the track point sensitivity
"""
import logging
import os
import time

FILES_ROOT = '/sys/devices/platform/i8042/serio1/serio2/'
CONFIG_FILE = '/etc/trackpointd.conf'


logging.basicConfig(level=logging.DEBUG)


def config_loader(path):
    conf = {}
    if not os.path.isfile(CONFIG_FILE):
        error = 'Config file %s does not exist' % CONFIG_FILE
        logging.error(error)
        raise RuntimeError(error)
    with open(path, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            line = line.strip()
            if not line.startswith('#') and len(line) > 0:
                option = tuple(map(str.strip, line.split('=', maxsplit=1)))
                if len(option) != 2:
                    error = 'Config error at line %d' % (i + 1)
                    logging.error(error)
                    raise RuntimeError(error)
                conf[os.path.join(FILES_ROOT, option[0])] = option[1]
    return conf


def main_loop(conf):
    while True:
        for file, value in conf.items():
            if os.access(file, os.R_OK):
                with open(file, 'r+') as f:
                    cur_val = f.read().strip()
                    if cur_val != value and os.access(file, os.W_OK):
                        logging.info('Writing %s to %s' % (value, file))
                        f.write(value)
        time.sleep(60)


if __name__ == '__main__':
    logging.info('trackpointd started')

    config = config_loader(CONFIG_FILE)
    time.sleep(15) # wait for the files to show up
    main_loop(config)
