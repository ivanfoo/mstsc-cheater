#! /usr/bin/env python

import os
import sys
from misc import Misc

class RemoteTerm:

    def __init__(self, targets = sys.argv[1:]):
        self.targets = targets
        self.datadir = os.path.dirname(__file__) + '/data/'

    def get_connect_data(self, host):
        filename = self.datadir + host + '.json'
        return Misc.load_json(filename)

    def set_cmd_keys(self):
        #some dos stuff
        pass

    def open_remote_term(self):
        #some dos stuff
        pass

    def run(self):
        for target in self.targets :
            data = self.get_connect_data(target)
            self.set_cmd_keys()
            self.open_remote_term()

rterm = RemoteTerm()
print 'Running rdos...'
rterm.run()