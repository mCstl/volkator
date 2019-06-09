#!/data/data/com.termux/files/usr/bin/python3
impors sys, os 
import urllib.request


print ('ok, lets start\n\n')
def lin(uri):
        print ('\n')
        f = open('text.txt')
        line = f.readline()
        for line in f:
                print(uri+line)
                try:
                        response = urllib.request.urlopen(uri+line)
                        resp = response.getcode()
                        if resp == 200:
                                print(response.getcode())
                                print(url+line+"  coe:"+response.getcode())

                except:
                        print ('no way.\n')
        f.close()

def test (site):
        if "http://" not in site and "https://"not in site:
                site = 'http://' + site
        if not url.endswith('/'):
                site = site + '/'
#       print (site)
        print ("site=> {}".format(site))

        try:
                response = urllib.request.urlopen(site)
                print ("\n\n Site is working allright")
                lin(site)
        except:
                print("\n\nThis site is not reacheble")
        exit()

url = input('SITE > ')
test(url)
