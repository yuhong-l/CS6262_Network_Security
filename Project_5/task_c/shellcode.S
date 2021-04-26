.extern _binary_payload_bin_start
.globl main
main:
jmp call

start:
/*popl %ebx get address of substituted attack body and xor table */
movl $_binary_payload_bin_start, %ebx /* copy the address to ecx */
movl %ebx, %ecx
addl $0x80, %ecx
movl $0x0,%edx
movl $0x0,%eax
subl $0x80,%esp


loop:
cmpl $0x20,%edx
jge run /* if (0x20<edx) goto skip */
movl (%ecx),%eax
xor (%ebx),%eax
movl %eax,(%esp)
add $0x4,%ebx /* move pointer to adjusted attack body */
add $0x4,%ecx /* move pointer to xor table */
add $0x4,%esp /* move pointer to result */
add $0x1,%edx
jmp loop

run:
/* print out decrypted code */
leal -0x80(%esp),%ecx
movl $0x80,%edx
movl $0x1,%ebx
xorl %eax,%eax
movl $0x4,%eax
int $0x80
/*quit*/
xorl %eax,%eax
inc %al
int $0x80

call:
call start
.string
