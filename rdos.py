#! /usr/bin/env python

import os
import sys
from helper import Helper
import subprocess

class RemoteWindoswsManager:

    def __init__(self, targets = sys.argv[1:]):
        self.targets = targets
        self.datadir = os.path.dirname(__file__) + '/data/'

    def get_connect_data(self, host):
        filename = self.datadir + host + '.json'    
        data = Helper.load_json(filename)
        return data

    def set_cmd_keys(self, data):
        host = "/generic:TERMSRV/" + data['host']
        user = "/user:" + data['user']
        passw = "/pass:" + Helper.get_decode_string(data['passw'])

        subprocess.call(['cmdkey', host, user, passw])
        return

    def open_remote_term(self, data):
        host = '/v:' + data['host']
        rdp = self.datadir + os.sep + data['rdp_file']
        subprocess.Popen(['mstsc', rdp, '/admin', host])
        return

    def run_target(self, target):
        data = self.get_connect_data(target)
        self.set_cmd_keys(data)
        self.open_remote_term(data)
        return

    def run(self):
        for target in self.targets:
            self.run_target(target)

rdos = RemoteWindoswsManager()

print 'Running rdos...'
rdos.run()
