#! /usr/bin/env python

import os
import sys
from misc import Misc

class RemoteWindoswsManager:

    def __init__(self, targets = sys.argv[1:]):
        self.targets = targets
        self.datadir = os.path.dirname(__file__) + '/data/'

    def get_connect_data(self, host):
        filename = self.datadir + host + '.json'        
        data = Misc.load_json(filename)
        data['passw'] = Misc.get_decode_string(data['passw'])
        return data

    def set_cmd_keys(self):
        #some dos stuff
        pass

    def open_remote_term(self):
        #some dos stuff
        pass

    def runTarget(self, target):
        data = self.get_connect_data(target)
        self.set_cmd_keys()
        self.open_remote_term()

    def run(self):
        for target in self.targets:
            self.runTarget(target)

rdos = RemoteWindoswsManager()

print 'Running rdos...'
rdos.run()
