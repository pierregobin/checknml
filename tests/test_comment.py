#!/usr/bin/python3

from lark import Lark
from lark import Token
from lark import Tree
#from .context import sample
from checknml import checknml_mod

def test_comment1():
    mem='''/* comment */ mem eDM[AMEM..START];'''
    s=checknml_mod.pdg_parser.parse(mem).find_data("mem_simple")
    t=next(s,None)
    print(t.children)
    assert t.children == [Token('MEM', 'mem'), Token('ID', 'eDM'), Tree('range', [Token('ID', 'AMEM'), Token('ID', 'START')])]
    #assert t == [Tree('mem_simple'),[Token('MEM', 'mem'), Token('ID', 'eDM'), Tree('range', [Token('NUMBER', '4'), Token('NUMBER', '1')])]]

def test_comment2():
    mem='''/* comment 
          */ 
          mem eDM[AMEM..START];'''
    s=checknml_mod.pdg_parser.parse(mem).find_data("mem_simple")
    t=next(s,None)
    print(t.children)
    assert t.children == [Token('MEM', 'mem'), Token('ID', 'eDM'), Tree('range', [Token('ID', 'AMEM'), Token('ID', 'START')])]
    #assert t == [Tree('mem_simple'),[Token('MEM', 'mem'), Token('ID', 'eDM'), Tree('range', [Token('NUMBER', '4'), Token('NUMBER', '1')])]]

test_comment1()
test_comment2()
