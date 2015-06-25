#! /usr/bin/env python

import json

class JsonHelper:

    @staticmethod
    def load_json_from_file(filename):
        with open(filename, 'r') as f:
            return json.load(f)

    @staticmethod
    def dump_json_to_file(items, filename):
        with open(filename, 'w') as f:
            json.dump(items, f, indent = 4, sort_keys = True)
            f.write('\n')
