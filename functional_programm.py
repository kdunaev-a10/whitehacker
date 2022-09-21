import argparse
import subprocess

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interfaces', dest='interfaceParse', help='Interface name to change mac' )
    parser.add_argument('-m', '--mac', dest='newmacParse', help='New MAC' )
    options = parser.parse_args()
    if not options.interfaceParse:
        parser.error('--specify interface name')
    elif not options.newmacParse:
        parser.error('--specify new MAC address')
    else:
        return options


def print_function(mac_new, int_name):
    print(mac_new, int_name)

opt = get_args()
print_function(opt.newmacParse, opt.interfaceParse)



#subprocess.call("sudo ifconfig", shell=True)