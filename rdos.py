#! /usr/bin/env python

import base64
import json
import os
import subprocess as s
import sys

class RemoteWindowsManager:

    def __init__(self, target):
        self.target = target
        self.datadir = os.path.dirname(__file__) + '/data/'
        self.data = []
        self.defport = '3389'
        self.defrpd = 'base.rdp'

    def get_connect_data(self):
        filename = self.datadir + self.target + '.json'

        with open(filename, 'r') as f:
            data = json.load(f)

        if 'port' not in data:
            data['port'] = self.defport
        if 'rdp' not in data:
            data['rdp'] = self.defrpd

        return data

    def set_cmdkeys(self):
        host = "/generic:TERMSRV/" + self.data['host']
        user = "/user:" + self.data['user']
        passw = "/pass:" + base64.b64decode(self.data['passw'])

        s.Popen(['cmdkey', host, user, passw], stdout=s.PIPE).wait()

    def del_cmdkeys(self):
        host = "/delete:TERMSRV/" + self.data['host']

        s.Popen(['cmdkey', host], stdout=s.PIPE).wait()

    def open_remote_desktop(self):
        host = '/v:' + self.data['host'] + ':' + self.data['port']
        rdp = self.datadir + self.data['rdp']

        s.Popen(['mstsc', rdp, '/admin', host]).wait()

    def run(self):
        self.data = self.get_connect_data()
        self.set_cmdkeys()
        self.open_remote_desktop()
        self.del_cmdkeys()

def main(target):
    rdos = RemoteWindowsManager(target)
    rdos.run()

if __name__ == '__main__':
    print 'Running rdos...\n'
    target = sys.argv[1]
    main(target)
