#! /usr/bin/env python

import base64
import os
import sys
import getpass
from rdos_helper import RdosHelper as Helper

class RemoteWindowsManager:

    def __init__(self, args):
        self.datadir = os.path.dirname(__file__) + "/data/"
        self.action = ""
        self.target = ""
        self.set_env(args)

    def add(self):
        data = {}
        data["host"] = raw_input("host: ")
        data["username"] = raw_input("username: ")
        data["passw"] = getpass.getpass()
        data["passw"] = base64.b64encode(data["passw"])
        
        self.set_target_data(data)

    def clear(self):
        host = self.get_target_data()["host"]
        Helper.del_cmdkeys(host)

    def open(self):
        data = self.get_target_data()
        data["passw"] = base64.b64decode(data["passw"])
        Helper.set_cmdkeys(data["host"], data["user"], data["passw"])
        Helper.connect()

    def rm(self):
        pass   

    def get_target_data(self):
        filename = self.datadir +  self.target + ".json"
        return Helper.load_json(filename)

    def set_target_data(self, items):
        filename = self.datadir +  self.target + ".json"
        Helper.dump_json(items, filename)

    def set_env(self, args):
        self.action = args[0]
        self.target = args[1]  

    def run(self):
        try:
            getattr(RemoteWindowsManager, self.action)(self)
        except AttributeError:
            print 'There is no such action'
        
def main(args):
    rdos = RemoteWindowsManager(args)
    rdos.run()

if __name__ == "__main__":
    print "\n### Running rdos... ###\n"
    main(sys.argv[1:])
