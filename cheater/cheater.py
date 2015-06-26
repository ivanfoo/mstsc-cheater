#! /usr/bin/env python

import sys
import importlib

class Cheater:

    def __init__(self):
        self.action = "open"
        self.target = ""

    def _get_object(self):
        module_name = "cheater.commands." + self.action
        try:
            module = importlib.import_module(module_name)
        except ImportError:
            print 'There is no such action'
            sys.exit(1)
        else:
            return getattr(module, self.action.capitalize())

    def run(self):
        Command = self._get_object()
        command = Command(self.target)
        command.run()

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

