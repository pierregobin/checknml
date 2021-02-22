#!/usr/bin/python3

from lark import Lark
from lark import Token
from lark import Tree
#from .context import sample
from checknml import checknml_mod

def test_spcomment1():
    mem="/*! comment */ mem eDM[AMEM..START];"
    s=checknml_mod.pdg_parser.parse(mem)
    print(s)
    #assert t.children == [Token('MEM', 'mem'), Token('ID', 'eDM'), Tree('range', [Token('ID', 'AMEM'), Token('ID', 'START')])]

def test_spcomment2():
    mem='''//! comment 
         mem eDM[AMEM..START];'''
    s=checknml_mod.pdg_parser.parse(mem)
    print(s)
    #assert t.children == [Token('MEM', 'mem'), Token('ID', 'eDM'), Tree('range', [Token('ID', 'AMEM'), Token('ID', 'START')])]

def test_spcomment3():
    mem='''/*! comment 
         */
         mem eDM[AMEM..START];'''
    s=checknml_mod.pdg_parser.parse(mem)
    print(s)
    #assert t.children == [Token('MEM', 'mem'), Token('ID', 'eDM'), Tree('range', [Token('ID', 'AMEM'), Token('ID', 'START')])]

test_spcomment1()
test_spcomment2()
test_spcomment3()
