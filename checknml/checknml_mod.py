#!/usr/bin/python3
from lark import Lark
 
pdg_parser=Lark('''start:  statement+
  statement :  memory

  memory: MEM ID  "[" range "]" ";"  -> mem_simple
        | MEM ID "[" range "]" code_block -> mem_code


  range : NUMBER ".." NUMBER
        | NUMBER
  code_block : "{"  instructions "}"
  INPORT : "inport" 
  OUTPORT : "outport" 
  port_declar : INPORT ID ";" | OUTPORT ID ";"
  instructions : (instruction*) 
  instruction : port_declar | INST
        | code_block
  INST:/[^{};]+/ ";"
  MEM : "mem"
  COMMENT: "//" /.+/
  NUMBER: /[0-9]+/
  ID : /_?[a-z][_a-z0-9]*/i
  %ignore COMMENT
  %import common.WS
  %import common.NEWLINE
  %ignore WS
''')
