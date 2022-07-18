import argparse
import subprocess

def pars():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interfaces', dest='interfaceParse', help='Interface name to change mac' )
    parser.add_argument('-m', '--mac', dest='newmacParse', help='New MAC' )
    return parser.parse_args()

def print_function(mac_new, int_name):
    print(mac_new, int_name)

opt = pars()
print_function(opt.newmacParse, opt.interfaceParse)



#subprocess.call("sudo ifconfig", shell=True)