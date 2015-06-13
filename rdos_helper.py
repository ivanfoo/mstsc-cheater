#! /usr/bin/env python

import json

class RdosHelper:

    @staticmethod
    def load_json(filename):
        with open(filename, 'r') as f:
            return json.load(f)

    @staticmethod
    def save_json(items, filename):
        with open(filename, 'w') as f:
            json.dump(items, f)

    

