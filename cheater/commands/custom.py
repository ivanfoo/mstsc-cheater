#! /usr/bin/env python

import base64
import cheater.config as config
from cheater.jsonhelper import JsonHelper as JHelper

class Custom

    def __init__(self, target):
        self.target = target

    def run(self):
        data = {
            "host": raw_input("host: "),
            "user": raw_input("user: "),
            "passw": base64.b64encode(getpass.getpass()),
            "port": raw_input("port: "),
            "rdp": raw_input("rdp file: ")
        }

        filename = config.targets_path + self.target + ".json"
        JHelper.dump_json_to_file(data, filename)
        KHelper.set_cmdkeys(data["host"], data["user"], base64.b64decode(data["passw"]))
