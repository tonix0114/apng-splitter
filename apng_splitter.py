#-*- coding:utf-8 -*-

import sys, struct

def parse(data):
	chunk = []
	data = data[8:]
	while data:
		length = struct.unpack('>I', data[:4])[0]
		chunk_data = data[:4]
		data = data[4:]
		
		chunk_type = data[:4]
		chunk_data += data[:4]
		data = data[4:]

		chunk_data += data[:length]
		data = data[length:]

		crc = struct.unpack('>I', data[:4])[0]
		chunk_data += data[:4]
		data = data[4:]

		chunk.append((str(chunk_type), str(length), chunk_data, hex(crc)))
	return chunk

"""
reference : http://stackoverflow.com/questions/16435740/how-can-i-split-animated-png-with-php

chunk
	[0] : type
	[1] : length
	[2] : data
	[3] : crc
"""

def main(): 
	name = sys.argv[1]
	with open(name, 'rb') as f: 
		data = f.read()
	signature = data[:8]
	if signature == "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a":
		chunk =  parse(data)
	
	count = 1
	IHDR = chunk[0]
	IEND = chunk[-1]

	for i in chunk[1:-1]:
		if i[0] == "fdAT":
			with open("apng_split_"+str(count)+".png","wb") as f:
				new_data = signature
				new_data += IHDR[2]
				new_data += i[2][:3] + chr(ord(i[2][3]) - 0x4)
				new_data += "IDAT"
				new_data += i[2][12:]
				new_data += IEND[2]	
				f.write(new_data)
			count += 1

	print "[+] Finished : " + str(count)

if __name__ == '__main__': 
	main()

