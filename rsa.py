#!/usr/bin/env python3
import subprocess
import sys


def check_prime(args):
    	p = int(args[2])
    	q = int(args[1])
    	n = args[0].replace(':', '=')

    	print(f"{n}{p}*{q}")


if len(sys.argv) != 2:
    print('Usage: rsa <file>')
    sys.exit(1)
else:
    with open(sys.argv[1], 'r') as file:
        for line in file:
            result = subprocess.check_output(['factor', line.strip()]
                                             ).decode('utf-8').split()
            check_prime(result)
