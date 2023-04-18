
from project_Inheritence_EXE.elf import Elf

class MuseElf(Elf):
    def __init__(self, username, level):
        super().__init__(username, level)


# elf = MuseElf("E", 4)
# print(str(elf))
# print(elf.__class__.__bases__[0].__name__)
# print(elf.username)
# print(elf.level)