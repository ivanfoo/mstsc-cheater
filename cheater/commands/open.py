#! /usr/bin/env python

import subprocess as sp
import cheater.config as config
from cheater.jsonhelper import JsonHelper as JHelper

class Open:

    def __init__(self, target):
        self.target = target

    def run(self):
        filename = config.targets_path + self.target + ".json"
        data = JHelper.load_json_from_file(filename)
        
        host = "/v:" + data["host"] + ":" + str(data["port"])

        if data["rdp"] == "":
            sp.Popen(["mstsc", "/admin", host]).wait()
        else:
            data["rdp"] = config.rdp + data["rdp"]
            sp.Popen(["mstsc", data["rdp"], "/admin", host]).wait()

