import register
import all_instr


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
    pass

def exec_opcode(opcode):
    all_instr.run(opcode)

class opcode_entry:

    def decode(self):
        return

    def exec(self):
        return

    width = 0

opcode_table = {










    
}

class cpu:

    general = general()

    segment = segment()

    eflags = register.group('32', EFLAGS)

    es = register.rtlreg_t()

    cs = register.uint16_r()

    eip = register.vaddr_t()

    class Decoding:
        eip = 0
        is_jmp = 0
        is_operand_size = 0
        src = opcode_entry()
        dest = opcode_entry()
        src2 = opcode_entry()

    decoding = Decoding()

    def init(self):

        return

    def decode(self):
        return

    def exec_wrapper(self):

        origin_eip = self.eip

        decoding.eip = origin_eip

        exec_real(decoding.eip)

        update_eip()

        return

    def exec_real(self, eip):
        opcode = instr_fetch(eip, 1)

        self.decoding.opcode = opcode

        set_width(opcode_table[opcode].width)

        idex(eip, opcode_table[opcode])

        return

    def fetch_instr(self):
        return

    def set_width(self, width):
        if width == 0:
            width = 2 if self.decoding.is_operand_size else 4
        decoding.src.width = decoding.dest.width = decoding.src2.width = width
        return

    def update_eip(self):
        if decoding.is_jmp:
            decoding.is_jmp = 0
        else:
            self.eip = self.decoding.eip

    def idex(self, eip, e):
        if e.decode:
            e.decode(eip)
        e.execute(eip)




