#!/usr/bin/python3

from lark import Lark
from lark import Token
from lark import Tree
#from .context import sample
from checknml import checknml_mod

def test():
    mem="mem eDM[4..1];"
    s=checknml_mod.pdg_parser.parse(mem).find_data("mem_simple")
    t=next(s,None)
     #print(t.children)
    assert t.children == [Token('MEM', 'mem'), Token('ID', 'eDM'), Tree('range', [Token('NUMBER', '4'), Token('NUMBER', '1')])]
    #assert t == [Tree('mem_simple'),[Token('MEM', 'mem'), Token('ID', 'eDM'), Tree('range', [Token('NUMBER', '4'), Token('NUMBER', '1')])]]


def test3():
    mem="mem T[5]{dm_ld: data=T[addr];}"
    s=checknml_mod.pdg_parser.parse(mem).find_data("mem_code")
    t=next(s,None)
    assert t.children==[Token('MEM', 'mem'), Token('ID', 'T'), Tree('range', [Token('NUMBER', '5')]), 
               Tree('code_block', [Tree('instructions', [Tree('instruction', [Token('INST', 'dm_ld: data=T[addr];')])])])]

test()
test3()
