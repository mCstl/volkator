#!/usr/bin/python3
impors sys, os, socket
import urllib.request

def res(host):
  try:
    socket.gethostbyname_ex(host)
    return True
  exept: return False

def main():
  host = sys.argv[1]
  if res(host):
  

if __name__ =='__main__':main();
