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
print(tree.pretty())
for i in tree.iter_subtrees():
    print (i)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
for d in ["MEM","ID","memory","range","mem_code","mem_simple","io_interface"]:
    print ("keyword " + d + " >>>>")
    for t in (tree.find_data(d)):
        print(t.children)
        print("==========\n")

