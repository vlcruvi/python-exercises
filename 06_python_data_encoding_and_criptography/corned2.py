#!/usr/bin/env python3

import sys
import hashlib

mist_hash = "e3cd7044ae6747a017866021a2033014cf4a3e989b6a4b45cdacd957b338e56fe68b84d004dc60ffff9dfc7789d22fbd5116250a9436a295e8d80e460666cb79"

hex_poss = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F' ]

permutations = ""
md5_try = ""
for hexa1 in hex_poss:
	for hexa2 in hex_poss:
		for hexa3 in hex_poss:
			permutation =  (str(hexa1) + str(hexa2) +str(hexa3))
			flag = "FS{hash-I_had_corned_beef_and_hash_" + permutation + "}"
			flag_object = hashlib.sha512(flag.encode())
			sha512_flag = flag_object.hexdigest()
			if mist_hash in sha512_flag:
				print(permutation)
		
