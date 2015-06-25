#! /usr/bin/env python

from cheater.jsonhelper import JsonHelper as Jhelper
import os
import base64
import subprocess as sp

class Open:

    def __init__(self, target):
        self.target = target

    def run(self):
        filename = os.path.dirname(__file__) + "/../resources/targets/" + self.target + ".json"
        data = Jhelper.load_json_from_file(filename)
        data["passw"] = base64.b64decode(data["passw"])

        if data["rdp"] != "":
            data["rdp"] = self.config["rdp_dir"] + data["rdp"]
        
        host = "/v:" + data["host"] + ":" + str(data["port"])

        if data["rdp"] == "":
            sp.Popen(["mstsc", "/admin", host]).wait()
        else:
            sp.Popen(["mstsc", data["rdp"], "/admin", host]).wait()

