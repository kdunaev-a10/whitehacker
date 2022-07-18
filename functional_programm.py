import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--interfaces', dest='interfaceParce', help='Interface name to change mac' )
parser.add_argument('-m', '--mac', dest='newmacParce', help='New MAC' )

options = parser.parse_args()

print(options,type(options), options.newmacParce)

#subprocess.call("sudo ifconfig", shell=True)