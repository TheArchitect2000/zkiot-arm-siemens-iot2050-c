	.arch armv8-a
	.file	"program.cpp"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
.LFB0:
	.cfi_startproc
#APP
// 16 "program.cpp" 1
	mov x18, #25
mov x17, #159
mul x17, x7, x18
add x17, x17, #28

// 0 "" 2
#NO_APP
	mov	w0, 0
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Debian 10.2.1-6) 10.2.1 20210110"
	.section	.note.GNU-stack,"",@progbits
