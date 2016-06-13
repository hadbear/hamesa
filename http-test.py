#!/usr/bin/env python
'''
makes an http connection
returns http status codes
checks path to dest
'''
import requests
import socket
import datetime as dt

class remote_host():
    def __init__(self, destination):
        '''set instance values for all attributes '''
        self.name = 'stub'
        self.ip, self.ipi = self.get_remote_ip(destination)
        self.status, self.headers = self.get_remote_host(destination)
        self.created = dt.datetime.now
        return None

    def get_remote_host(self, dest):
        rw = 'http://%s/' % dest
        noconnection = (500, {})
        try:
            r = requests.head(rw, timeout=0.01)
        except requests.exceptions.ConnectionError:
            return noconnection
        except requests.exceptions.ReadTimeout:
            return noconnection
        try:
            r.close()
        except UnboundLocalError:
            return noconnection
        return r.status_code, r.headers

    def get_remote_ip(self, dest):
        try:
            dest_ipi = socket.inet_aton(dest)
            dest_ip = socket.gethostbyaddr(dest)
        except socket.error:
            dest_ip = '0.0.0.0'
            dest_ipi = 0
        return dest_ip, dest_ipi



if __name__ == "__main__":
    switch_list = ['10.1.10.30', 
                   '10.1.10.31',
                   '10.1.10.32', 
                   '10.1.10.12', 
                   '10.1.10.25', 
                   '10.1.10.26' ]
    so = [] 
    for i in switch_list:
        so.append(remote_host(i))
    # sw1 = remote_host('10.1.10.32')
    for i in so:
        print so[i].status
        print so[i].headers
    print i
