#!/usr/bin/python3

import sys
from dns import resolver


def doms(host):
        list = open(sys.argv[2], 'a+')
        dom = ['.com', '.de', '.cn', '.uk', '.net', '.org', '.info', '.ru', '.nl', '.tk', '.asia', '.su', '.social', '.co.uk', '.mobi', '.biz','.cat', '.edu', '.gov', '.info', '.jobs', '.net', '.name', '.one', '.ooo', '.photo', '.pics', '.feedback', '.place', '.plus', '.pro', '.production', '.red', '.ren', '.rent', '.report', '.rest', '.rich', '.site', '.tel', '.xxx', '.travel', '.xyz', '.zone', '.yoga', '.ninja', '.li', '.moe', '.yandex', '.art']
        url = host.split('.')[0]
        for rdom in dom:
                if res(url + rdom):
                        print(url+rdom)
                        list.write(url+'\n')
                        list.flush()
                else: pass

def res(host):
  res = resolver.Resolver()
  res.nameservers = ['1.1.1.1']
  try:
    answers = res.query(host)
    #for rdata in answers:
    #print (rdata.address)
    return True
  except: return False

def main():
        host = sys.argv[1]
        if res(host):
                doms(host)

if __name__ =='__main__': main();
