#@author capa
#@category Analysis
#@menupath Tools.Run capa analysis
#@keybinding

from ghidra.program.model.listing import Program

program = currentProgram

if not program:
    print("No program loaded")
else:
    print("PyGhidra execution OK")
    print("Program:", program.getName())
    print("Functions:", program.getFunctionManager().getFunctionCount())