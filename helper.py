#! /usr/bin/env python

import json
import base64

class Helper:

    @staticmethod
    def items_to_lower(items):
        for i, item in enumerate(items):
            items[i] = item.lower()
        return items
        
    @staticmethod
    def load_json(filename):
        with open(filename, 'r') as f:
            content = json.load(f)

        return content

    @staticmethod
    def decode_string(string):
        return base64.b64decode(string)



