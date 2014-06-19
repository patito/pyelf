import mmap
import os.path
from utils import Singleton

@Singleton
class LoadELFFile(object):
    """
    ELFFile class is responsible to load binary file using
    mmap.

    """

    def __init__(self, filename):
        if os.path.isfile(filename) == True:
            f = open(filename, "rb")
            self.__mem = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            self.__binary_data = bytearray(self.__mem)
        else:
            print "Wrong filename bitch!"

    @property
    def binary(self):
        return self.__binary_data

    def __del__(self):
        self.__mem.close()
