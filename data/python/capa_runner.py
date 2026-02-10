from ghidra.program.model.listing import Program

def run(program: Program):
    """
    Called from Java via PyGhidra.
    Program is already analyzed.
    """

    name = program.getName()
    funcs = program.getFunctionManager().getFunctionCount()

    return f"""
    capa MVP PyGhidra test OK

    Program: {name}
    Functions: {funcs}
    """