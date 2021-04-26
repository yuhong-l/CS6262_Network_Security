

a.out: shellcode.o payload.o
	gcc -g3 -m32 shellcode.o payload.o -o a.out
shellcode.o: shellcode.S
	gcc -g3 -c shellcode.S -m32 -o shellcode.o

payload.o: payload.bin
	objcopy -I binary -O elf32-i386 -B i386 payload.bin payload.o

