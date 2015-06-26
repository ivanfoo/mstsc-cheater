#! /usr/bin/env python

import cheater.config as config
from cheater.jsonhelper import JsonHelper as JHelper
from cheater.keyshelper import KeysHelper as KHelper

class Clear:

    def __init__(self, target):
        self.target = target

    def run(self):
        filename = config.targets_path + self.target + ".json"
        host = JHelper.load_json_from_file(filename)["host"]
        KHelper.del_cmdkeys(host)
