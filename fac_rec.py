import prettydiasm

def fac(arg_n=7):
    if arg_n == 1:
        return arg_n
    return arg_n * fac(arg_n - 1)

print( "prettydiasm.prettydis(fac, show_opcode_as_links=True):", prettydiasm.prettydis(fac, show_opcode_as_links=True) )
