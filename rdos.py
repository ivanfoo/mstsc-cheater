#! /usr/bin/env python

import base64
import json
import os
import subprocess as s
import sys

class RemoteWindowsManager:

    def __init__(self, target, datadir):
        self.target = target
        self.datadir = datadir
        self.data = []

    def get_connect_data(self):
        filename = self.datadir + self.target + '.json'
        with open(filename, 'r') as f:
            data = json.load(f)
        return data

    def set_cmdkeys(self):
        host = "/generic:TERMSRV/" + self.data['host']
        user = "/user:" + self.data['user']
        passw = "/pass:" + base64.b64decode(self.data['passw'])
        s.Popen(['cmdkey', host, user, passw], stdout=s.PIPE).wait()

    def del_cmdkeys(self):
        host = "/delete:TERMSRV/" + self.data['host']
        s.Popen(['cmdkey', host], stdout=s.PIPE).wait()

    def open_remote_term(self):
        host = '/v:' + self.data['host']
        rdp = self.datadir + self.data['rdp_file']
        s.Popen(['mstsc', rdp, '/admin', host]).wait()

    def run(self):
        self.data = self.get_connect_data()
        self.set_cmdkeys()
        self.open_remote_term()
        self.del_cmdkeys()

def main(target, datadir):
    rdos = RemoteWindowsManager(target, datadir)
    rdos.run()

if __name__ == '__main__':
    print 'Running rdos...'
    datadir = os.path.dirname(__file__) + '/data/'
    target = sys.argv[1]
    main(target, datadir)
