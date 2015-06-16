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
        self.data = {}
        self.args = args
        self.datadir = os.path.dirname(__file__) + "/data/"
        self.cmd = ""
        self.target = ""
        self.cmd_list = {
            "add": "add_cmd",
            "edit": "edit_cmd",
            "clear": "clear_cmd",
            "open": "open_cmd",
            "rm": "rm_cmd"
        }

    def get_target_data(self):
        filename = self.datadir +  self.target + ".json"
        return Helper.load_json(filename)

    def set_target_data(self, items):
        filename = self.datadir +  self.target + ".json"
        Helper.dump_json(items, filename)

    def set_env(self):
        if self.args[0] not in self.cmd_list:
            target = self.args[0]
            self.args[0] = "open"
            self.args.append(target)

        self.cmd = self.args[0]
        self.target = self.args[1]

    def add_cmd (self):
        target_data = {}
        target_data["host"] = raw_input("host: ")
        target_data["username"] = raw_input("username: ")
        target_data["password"] = getpass.getpass()
        
        self.set_target_data(target_data)

    def open_cmd(self):
        self.data = self.get_target_data()
        Helper.set_cmdkeys()
        Helper.connect()

    def rm_cmd(self):
        pass     

    def run(self):
        self.set_env()
        getattr(RemoteWindowsManager, self.cmd_list[self.cmd])(self)
        
def main(args):
    rdos = RemoteWindowsManager(args)
    rdos.run()

if __name__ == "__main__":
    print "\n### Running rdos... ###\n"
    args = sys.argv[1:]
    main(args)
