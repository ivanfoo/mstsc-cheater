#!/usr/bin/env python

import json

class Misc:

    @staticmethod
    def load_json(filename):

        with open(filename, 'r') as f:
            content = json.load(f)
        f.close()

        return content

    @staticmethod
    def run_dos_command():
        pass
