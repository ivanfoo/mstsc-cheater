#! /usr/bin/env python

import json
import subprocess as s

class Helper:

    @staticmethod
    def load_json(filename):
        with open(filename, 'r') as f:
            return json.load(f)

    @staticmethod
    def dump_json(items, filename):
        with open(filename, 'w') as f:
            json.dump(items, f, indent = 4)
            f.write('\n')

    @staticmethod
    def set_cmdkeys(host, user, passw):
        host = "/generic:TERMSRV/" + host
        user = "/user:" + user
        passw = passw = "/pass:" + passw
        s.Popen(["cmdkey", host, user, passw], stdout = s.PIPE).wait()

    @staticmethod
    def del_cmdkeys(self, host):
        host = "/delete:TERMSRV/" + host
        s.Popen(["cmdkey", host], stdout = s.PIPE).wait()

    @staticmethod
    def connect(self, data):
        host = "/v:" + data["host"] + ":" + data["port"]
        s.Popen(["mstsc", data["rdp"], "/admin", host]).wait()



    

