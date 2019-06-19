#!/usr/bin/python3

import sys, requests
from dns import resolver


def doms(host):
	list = open(sys.argv[2], 'a+')
		dom = ['.com', '.de', '.cn', '.uk', '.net', '.org', '.info', '.ru', '.nl', '.tk', '.asia', '.su', '.social', '.co.uk', '.mobi', '.biz','.cat', '.edu', '.gov', '.info', '.jobs', '.net', '.name', '.one', '.ooo', '.photo', '.pics', '.feedback', '.place', '.plus', '.pro', '.production', '.red', '.ren', '.rent', '.report', '.rest', '.rich', '.site', '.tel', '.xxx', '.travel', '.xyz', '.zone', '.yoga', '.ninja', '.li', '.moe', '.yandex', '.art']
		url = host.split('.')[0]
		for rdom in dom:
			if res(url + rdom):
				print(url+rdom)
				get(url+dom)
				#list.write(url+'\n')
				#list.flush()
			else: pass
def get(dhost):
	try:
		r = requests.get(dhost)
		if int(r.status_code) < 199 or int(r.status_code) > 399:
			if fuzz(dhost):
				list.write(link)
            else:pass
	except: fuzz(dhost)
    
def fuzz(dhost):
	byte = ['.', '%00', 'i', 'en', 'index.php', 'readme.html', '0x0000', '%2500']
    
	try:
		for i in (0, len(byte)):
			link = (dhost + '/' + byte[i])
			rf = requests.get(link)
			if int(rf.status_code) in (200, 399):
				return link
			else:pass
            
            
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
