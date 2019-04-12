#!/usr/bin/env python3
"""
The daemon for automatically set the track point sensitivity
"""
import logging
import os
import time

CONFIG_FILE = '/etc/trackpointd.conf'
WAIT_TIMEOUT = 60 # Wait 60 seconds for a file to show up


logging.basicConfig(level=logging.DEBUG)


def config_loader(path):
    conf = {}
    if not os.path.isfile(CONFIG_FILE):
        error = 'Config file %s does not exist' % CONFIG_FILE
        raise RuntimeError(error)
    with open(path, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            comment_idx = line.find('#')
            if comment_idx != -1:
                line = line[:comment_idx]
            line = line.strip()
            if not line.startswith('#') and len(line) > 0:
                option = tuple(map(str.strip, line.split('=', maxsplit=1)))
                if len(option) != 2:
                    error = 'Config error at line %d' % (i + 1)
                    raise RuntimeError(error)
                conf[option[0]] = option[1]
    return conf


def main_loop(config_path):
    while True:
        config = config_loader(config_path)
        dir = config.pop('dir', None)
        if dir is None:
            raise RuntimeError(
                    'You need to specify where the hardware settings are'
            )
        for file, value in config.items():
            file = os.path.join(dir, file)

            for i in range(WAIT_TIMEOUT):
                if os.access(file, os.R_OK):
                    break
                time.sleep(1)
            else:
                raise RuntimeError('File %s does not exist' % file)

            with open(file, 'r+') as f:
                cur_val = f.read().strip()
                if cur_val != value and os.access(file, os.W_OK):
                    logging.info('Writing %s to %s' % (value, file))
                    f.write(value)
        time.sleep(60)


if __name__ == '__main__':
    time.sleep(5)
    main_loop(CONFIG_FILE)

