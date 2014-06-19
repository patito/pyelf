import mmap
from elf import LoadELFFile

class Ident(object):
    """
    Ident is an ELF Identification class.

    """
    EI_MAG0    = 0
    EI_MAG1    = 1
    EI_MAG2    = 2
    EI_MAG3    = 3
    EI_CLASS   = 4
    EI_DATA    = 5
    EI_VERSION = 6
    EI_PAD     = 7

    def __init__(self):
        self.__elf = LoadELFFile(None)
        self.__binary_data = self.__elf.binary

    @property
    def ei_mag0(self):
        return format(self.__binary_data[self.EI_MAG0], '02x') 

    @property
    def ei_mag1(self):
        return self.__binary_data[self.EI_MAG1]

    @property
    def ei_mag2(self):
        return self.__binary_data[self.EI_MAG2]
    
    @property
    def ei_mag3(self):
        return self.__binary_data[self.EI_MAG3]

    @property
    def ei_class(self):
        return self.__binary_data[self.EI_CLASS]

    @property
    def ei_data(self):
        return self.__binary_data[self.EI_DATA]

    @property
    def ei_version(self):
        return self.__binary_data[self.EI_VERSION]
    
    @property
    def ei_pad(self):
        return self.__binary_data[self.EI_PAD]

    def is_elf(self):
        return (self.ei_mag0 == "7f") and (self.__binary_data[1:4] == "ELF")

    def __str__(self):
        x = "ELF Identification:\n"
        x += "  EI_MAG0    = %s\n" % self.ei_mag0
        x += "  EI_MAG1    = %c\n" % self.ei_mag1
        x += "  EI_MAG2    = %c\n" % self.ei_mag2
        x += "  EI_MAG3    = %c\n" % self.ei_mag3
        x += "  EI_CLASS   = %s\n" % self.ei_class
        x += "  EI_DATA    = %s\n" % self.ei_data
        x += "  EI_VERSION = %s\n" % self.ei_version
        x += "  EI_PAD     = %s\n" % self.ei_pad
        return x

    def __repr__(self):
        return str(self)

