#!/usr/bin/python3
import os
import argparse

from checknml import checknml_mod

argcli = argparse.ArgumentParser(description='check nml/pdg description')
argcli.add_argument("--file", metavar='path',type=str, help="the file to be checked")
argcli.add_argument("--string", type=str, help="the file to be checked")
args=argcli.parse_args()

if args.string != None :
    s = args.string
elif args.file != None:
    f = open(args.file)
    s = f.read()
    f.close()

tree= checknml_mod.pdg_parser.parse(s)
print(tree)

checknml_mod.showPosition().visit_topdown(tree)

