import mmap
from elf import LoadELFFile
import binascii

class Ehdr(object):
    """
    ELF Header.

    """

    E_TYPE = 16
    E_MACHINE = 18
    E_VERSION = 20
    E_EHSIZE = 40
    E_PHENTSIZE = 42

    def __init__(self):
        self.__elf = LoadELFFile(None)

    @property
    def e_type(self):
        return binascii.hexlify(str(self.__elf.binary[17:15:-1]))

    @property
    def e_machine(self):
        return self.__elf.binary[self.E_MACHINE]    
    
    @property
    def e_version(self):
        return self.__elf.binary[self.E_VERSION]    

    @property
    def e_entry(self):
        return "0x" + str(self.__elf.binary[27:23:-1]).encode('hex')

    @property
    def e_phoff(self):
        return "0x" + str(self.__elf.binary[31:27:-1]).encode('hex')

    @property
    def e_shoff(self):
        return "0x" + str(self.__elf.binary[35:31:-1]).encode('hex')

    @property
    def e_ehsize(self):
        return binascii.hexlify(str(self.__elf.binary[41:39:-1]))

    @property
    def e_phentsize(self):
        return binascii.hexlify(str(self.__elf.binary[43:41:-1]))


