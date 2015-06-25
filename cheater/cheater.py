#! /usr/bin/env python

import base64
import os
import sys
import getpass
from helper import Helper
import importlib
# import commands.open as _open

class Cheater:

    def __init__(self):
        self.config = {
            "port": 3389,
            "rdp": "",
            "target_dir": os.path.dirname(__file__) + "/resources/targets/",
            "rdp_dir": os.path.dirname(__file__) + "/resources/rdps/"
        }

        self.action = ""
        self.target = ""

    def _add(self):
        data = {
            "host": raw_input("host: "),
            "user": raw_input("user: "),
            "passw": base64.b64encode(getpass.getpass())
        }

        data["port"] = self.config["port"]
        data["rdp"] = self.config["rdp"]

        self._dump_target_data(data)
        Helper.set_cmdkeys(data["host"], data["user"], base64.b64decode(data["passw"]))

    def _add_custom(self):
        data = {
            "host": raw_input("host: "),
            "user": raw_input("user: "),
            "passw": base64.b64encode(getpass.getpass()),
            "port": raw_input("port: "),
            "rdp": raw_input("rdp file: ")
        }

        self._dump_target_data(data)
        Helper.set_cmdkeys(data["host"], data["user"], base64.b64decode(data["passw"])) 

    def _clear(self):
        host = self._load_target_data()["host"]
        Helper.del_cmdkeys(host)

    def _open(self):
        data = self._load_target_data()
        data["passw"] = base64.b64decode(data["passw"])

        if data["rdp"] != "":
            data["rdp"] = self.config["rdp_dir"] + data["rdp"]

        Helper.connect(data)

    def _rm(self):
        host = self._load_target_data()["host"]
        Helper.del_cmdkeys(host)
        filename = self.config["target_dir"] +  self.target + ".json"
        os.remove(filename)

    def _load_target_data(self):
        filename = self.config["target_dir"] +  self.target + ".json"
        return Helper.load_json(filename)

    def _dump_target_data(self, items):
        filename = self.config["target_dir"] +  self.target + ".json"
        Helper.dump_json(items, filename)

    def _define_env(self, args):
        if len(args) == 1:
            args.append(args[0])
            args[0] = "open"

        self.action = "_" + args[0]
        self.target = args[1]  

    def run_old(self, args):
        try:
            getattr(Cheater, self.action)(self)
        except AttributeError:
            print "There is no such action"

    def run(self):
        module_name = "commands" + "." + self.action
        print module_name
        exit()
        module = importlib.import_module(module_name)
        command = getattr(module, self.action.capitalize())(self.target)
        command.run()
        #Open = commands.open.Open(self.target)
        #Open.run()

def main(args = None):
    if args is None:
        args = sys.argv[1:]

    if len(args) == 1:
        args.append(args[0])
        args[0] = "open"

    cheater = Cheater()
    cheater.action = args[0]
    cheater.target = args[1]
    cheater.run()

