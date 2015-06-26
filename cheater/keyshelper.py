#! /usr/bin/env python

import subprocess as sp

class KeysHelper:

    @staticmethod
    def set_cmdkeys(host, user, passw):
        host = "/generic:TERMSRV/" + host
        user = "/user:" + user
        passw = passw = "/pass:" + passw
        sp.Popen(["cmdkey", host, user, passw], stdout = sp.PIPE).wait()

    @staticmethod
    def del_cmdkeys(host):
        host = "/delete:TERMSRV/" + host
        sp.Popen(["cmdkey", host], stdout = sp.PIPE).wait()
