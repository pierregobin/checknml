#!/usr/bin/python3
import argparse

from checknml import checknml_mod

argcli = argparse.ArgumentParser(description='check nml/pdg description')
argcli.add_argument("--file", metavar='path',type=str, help="the file to be checked")
argcli.add_argument("--string", type=str, help="the file to be checked")
args=argcli.parse_args()

print(args.string)
