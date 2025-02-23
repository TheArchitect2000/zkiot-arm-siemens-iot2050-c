// program.cpp
int main() {
    asm volatile (
        "mov x18, #314\n"
        "mov x17, #159\n"
        "mul x17, x17, x18\n"
        "add x17, x17, #26\n"
    );
    return 0;
}