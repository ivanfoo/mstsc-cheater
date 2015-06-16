#! /usr/bin/env python

import base64
import json
import os
import subprocess as s
import sys
import time
import getpass
from rdos_helper import RdosHelper as Helper

class RemoteWindowsManager:

    def __init__(self, args):
        self.args = args
        self.datadir = os.path.dirname(__file__) + '/data/'
        self.action = ''
        self.target = ''

        self.existing_actions = { "add": "add_cmd", "edit": "edit_cmd", "clear": "clear_cmd", "open": "open_cmd", "rm": "rm_cmd"}

    def get_target_data(self):
        filename = self.datadir +  self.target + '.json'
        return Helper.load_json(filename)

    def set_target_data(self, items):
        filename = self.datadir +  self.target + '.json'
        Helper.save_json(items, filename)

    def set_env(self):
        if self.args[0] not in self.existing_actions:
            target = self.args[0]
            self.args[0] = 'open'
            self.args.append(target)

        self.action = self.args[0]
        self.target = self.args[1]

    def add_cmd (self):
        items = {}
        items['host'] = raw_input("host: ")
        items['username'] = raw_input("username: ")
        items['password'] = getpass.getpass()
        
        self.set_target_data(items)

    def open_cmd(self):
        self.data = self.get_target_data()
        #self.set_cmdkeys()
        #self.connect()
        #self.clear()

    def rm_cmd(self):
        pass     

    def set_cmdkeys(self):
        host = "/generic:TERMSRV/" + self.data['host']
        user = "/user:" + self.data['user']
        passw = "/pass:" + base64.b64decode(self.data['passw'])

        s.Popen(['cmdkey', host, user, passw], stdout=s.PIPE).wait()

    def del_cmdkeys(self):
        host = "/delete:TERMSRV/" + self.data['host']

        s.Popen(['cmdkey', host], stdout=s.PIPE).wait()

    def connect(self):
        host = '/v:' + self.data['host'] + ':' + self.data['port']
        rdp = self.datadir + self.data['rdp']

        s.Popen(['mstsc', rdp, '/admin', host]).wait()

    def run(self):
        self.set_env()
        getattr(RemoteWindowsManager, self.existing_actions[self.action])(self)
        
def main(target):
    rdos = RemoteWindowsManager(target)
    rdos.run()

if __name__ == '__main__':
    print '\n### Running rdos... ###\n'
    args = sys.argv[1:]
    main(args)
