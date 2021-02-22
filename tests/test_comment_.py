#!/usr/bin/python3

from lark import Lark
from lark import Token
from lark import Tree
#from .context import sample
from checknml import checknml_mod

def test_comment1():
    mem='''/* comment */ mem edm;'''
    s=checknml_mod.basic_parser.parse(mem)
    print(s)
    #assert t == [Tree('mem_simple'),[Token('MEM', 'mem'), Token('ID', 'eDM'), Tree('range', [Token('NUMBER', '4'), Token('NUMBER', '1')])]]

def test_comment2():
    mem='''
          mem a;
          /* comment 
          */ 
          mem e;'''
    s=checknml_mod.basic_parser.parse(mem)
    print(s)

#test_comment1()
test_comment2()
