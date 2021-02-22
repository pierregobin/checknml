#!/usr/bin/python3
from lark import Lark
from lark import Visitor
 
pdg_parser=Lark('''start:  statement*
  statement :  memory
            | io_interface
            | SPECIAL_COMMENT

  memory: MEM ID  "[" range "]" ";"  -> mem_simple
        | MEM ID "[" range "]" code_block -> mem_code


  range : (NUMBER|ID) ".." (NUMBER|ID)
        | (NUMBER|ID)
  code_block : "{"  instructions "}"
  io_interface : IO ID "(" param_list ")" "{" memory* port* process* "}"
  IO : "io_interface"
  param_list : ID ("," ID)*

  port : (INPORT|OUTPORT) ID ";"
  process : PROCESS  "(" ")" code_block
  PROCESS : /process_[a-zA-Z_0-9]+/
  INPORT : "inport" 
  OUTPORT : "outport" 
  port_declar : INPORT ID ";" | OUTPORT ID ";"
  instructions : (instruction*) 
  instruction : port_declar | INST
        | code_block
  INST:/[^{};]+/ ";"
  MEM : "mem"
  SPECIAL_COMMENT: "//!" /.+/
      | "/*!" /(.|\\n)*/x "*/"
      | "{{" /(.|\n)*/x "}}"
      | "/*!" /.+/ "*/"
  COMMENT: "//" /.+/
        | "/*" /(.|\\n|\\r)+/ "*/"
  NUMBER: /[0-9]+/
  ID : /_?[a-z][_a-z0-9]*/i
  %ignore COMMENT
  %import common.WS
  %import common.NEWLINE
  %ignore WS
  %ignore NEWLINE
''',
parser="lalr" ,
propagate_positions=True)

basic_parser=Lark('''
  start : statement*
  statement : memory
  memory: MEM ID ";"
  MEM : "mem"
  ID : /[a-z][a-z0-9]*/
  NUMBER: /[0-9]+/
  COMMENT : "/*" /(.|\\n|\\r)+/ "*/"
  %ignore COMMENT
  %import common.WS
  %import common.NEWLINE
  %ignore NEWLINE
  %ignore WS
        ''')

class showPosition(Visitor):
    def __default__(self,tree):
        print ([tree.data ,  tree.children ,tree.line,tree.column])
