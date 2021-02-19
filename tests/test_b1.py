
#from .context import sample
from checknml import checknml_mod

def test_mem():
    mem="mem eDM[4..1];"
    s=checknml_mod.pdg_parser.parse(mem).pretty()
    assert s == "start\n  sta\n    mem\n    eDM\n    range\n      4\n      1\n"
