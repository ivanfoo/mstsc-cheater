#!/usr/bin/env python

import json
import subprocess
import base64   

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

    @staticmethod
    def get_decode_string(string):
        return base64.b64decode(string)

