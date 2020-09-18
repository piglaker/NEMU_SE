import device
import cpu
import memory

def main():
    CPU = cpu.init()
    MEMORY = memory.init()
    CPU.mem = MEMORY
    CPU.run()

if __name__ == '__main__':
    main()
