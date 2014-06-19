import mmap
from elf import LoadELFFile
import binascii

class Ehdr(object):
    """
    ELF Header.

    """

    def __init__(self):
        self.__elf = LoadELFFile(None)

    @property
    def e_type(self):
        return binascii.hexlify(str(self.__elf.binary[17:15:-1]))

    @property
    def e_machine(self):
        return binascii.hexlify(str(self.__elf.binary[19:17:-1]))
    
    @property
    def e_version(self):
        return binascii.hexlify(str(self.__elf.binary[23:19:-1]))

    @property
    def e_entry(self):
        return binascii.hexlify(str(self.__elf.binary[27:23:-1]))

    @property
    def e_phoff(self):
        return binascii.hexlify(str(self.__elf.binary[31:27:-1]))

    @property
    def e_shoff(self):
        return binascii.hexlify(str(self.__elf.binary[35:31:-1]))

    @property
    def e_ehsize(self):
        return binascii.hexlify(str(self.__elf.binary[41:39:-1]))

    @property
    def e_phentsize(self):
        return binascii.hexlify(str(self.__elf.binary[43:41:-1]))
    
    @property
    def e_phnum(self):
        return binascii.hexlify(str(self.__elf.binary[45:43:-1]))

    @property
    def e_shentsize(self):
        return binascii.hexlify(str(self.__elf.binary[47:45:-1]))

    @property
    def e_shnum(self):
        return binascii.hexlify(str(self.__elf.binary[49:47:-1]))

    @property
    def e_shstrndx(self):
        return binascii.hexlify(str(self.__elf.binary[51:49:-1]))




