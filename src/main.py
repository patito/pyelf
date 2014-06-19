from elf import LoadELFFile, Ident
from elf import Ehdr

l = LoadELFFile("/bin/bash")
e = Ehdr()
print e.e_type
print e.e_machine
print e.e_version
print e.e_entry
print e.e_phoff
print e.e_shoff
print e.e_ehsize
print e.e_phentsize
print int(str(e.e_shstrndx), 0)
