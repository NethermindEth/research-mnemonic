from shamir import * 
import galois
import sys
from random import randint
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-ns', type=int, help='number of secret', required=True)
parser.add_argument('-nt', type=int, help='number of threshold', required=True)

args = parser.parse_args()

if (args.ns < args.nt):
	print('error: ns cannot be lower than nt')
	sys.exit(0)



print(args.ns)

