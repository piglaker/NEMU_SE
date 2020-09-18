import register

EFLAGS = "CF:1, R1:1, PF:1, R2:1, AF:1, R3:1, ZF:1, SF:1, TF:1, IF:1, DF:1, OF:1, IOPL:1, \
        NT:1, R4:1, RF:1, VM:1, AC:1, VIF:1, VIP:1, ID:1, R5:10"

General_Registers = {'32':"EAX, EBX, ECX, EDX", '16':"AX, BX, CX, DX", '8':"AH,AL,BH,BL,CH,CL,DH,DL"}

Segment_Registers = "CS, DS, ES, FS, GS, SS"

Index_pointers = "ESI, EDI, EBP, EIP, ESP"

class general:
    _32 = register.group('32', General_Registers['32'])
    _16 = register.group('16', General_Registers['16'])
    _8 = register.group('8', General_Registers['8'])

class segment:
    


class cpu:

    general = general()

    segment = segment()

    eflags = register.group('32', EFLAGS)

    es = register.rtlreg_t()

    cs = register.uint16_r()

    eip = register.vaddr_t()




