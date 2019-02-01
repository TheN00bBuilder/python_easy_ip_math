#!/usr/bin/env python3

import argparse
import ipaddress

parser = argparse.ArgumentParser()
parser.add_argument("bip", type = str, help = "Put in your beginning IP with subnet here.")
parser.add_argument("--v", action = 'store_true', help = "Set verbose to print all possible IP addresses with specified subnet. No flag will only print a range value.")
args = parser.parse_args()

bip = args.bip
verbose = args.v

if bip == None:
    print("Add an IP!")
else:
    try:
        address = ipaddress.IPv4Network(bip, strict=False)
    except ValueError as e:
        print("This is not a valid IP range: %s" % e)
    else:
        if verbose == True:
            for ip in address:
                print(ip)
            print('Usable Range: %s - %s' % (address[0]+1, address[-1]-1))
        else:
            print('Usable Range: %s - %s' % (address[0]+1, address[-1]-1))