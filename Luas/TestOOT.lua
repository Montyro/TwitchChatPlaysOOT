memory.usememorydomain("RDRAM")

while true do
	memory.writebyte(0x11A64B,0x0F)
	emu.frameadvance()
	--console.writeline("memory.writebyte(0x11A64B,0x00)")
end
--memory.writebyte(0x11A64B,0)
--v = comm.getluafunctionslist()
--console.writeline(v)
--socket_ip=127.0.0.1 --socket_port=65432