memory.usememorydomain("RDRAM")
while true do 
	 memory.write_s16_be(0x11A604,0x42)
	 emu.frameadvance()
end