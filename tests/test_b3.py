#!/usr/bin/python3

from lark import Lark
from lark import Token
from lark import Tree
#from .context import sample
from checknml import checknml_mod

def test():
    mem="mem eDM[AMEM..START];"
    s=checknml_mod.pdg_parser.parse(mem).find_data("mem_simple")
    t=next(s,None)
     #print(t.children)
    assert t.children == [Token('MEM', 'mem'), Token('ID', 'eDM'), Tree('range', [Token('ID', 'AMEM'), Token('ID', 'START')])]
    #assert t == [Tree('mem_simple'),[Token('MEM', 'mem'), Token('ID', 'eDM'), Tree('range', [Token('NUMBER', '4'), Token('NUMBER', '1')])]]


def test3():
    mem="mem T[SIZE]{dm_ld: data=T[addr];}"
    s=checknml_mod.pdg_parser.parse(mem).find_data("mem_code")
    t=next(s,None)
    assert t.children==[Token('MEM', 'mem'), Token('ID', 'T'), Tree('range', [Token('ID', 'SIZE')]), 
               Tree('code_block', [Tree('instructions', [Tree('instruction', [Token('INST', 'dm_ld: data=T[addr];')])])])]

def test_io():
    m="io_interface truc (a,b,aa) { mem eDM[4]; inport i_a; process_request(){a=b;}}"
    s=checknml_mod.pdg_parser.parse(m).find_data("io_interface")
    t=next(s,None)
    assert t.children == [Token('IO', 'io_interface'), Token('ID', 'truc'), 
            Tree('param_list', [Token('ID', 'a'), Token('ID', 'b'),  Token('ID', 'aa')]), 
            Tree('mem_simple', [Token('MEM', 'mem'), Token('ID', 'eDM'),  Tree('range', [Token('NUMBER', '4')])]), 
            Tree('port', [Token('INPORT', 'inport'),  Token('ID', 'i_a')]), 
            Tree('process',  [Token('PROCESS', 'process_request'),  
                Tree('code_block', [Tree('instructions',  [Tree('instruction', [Token('INST', 'a=b;')])])])])]
