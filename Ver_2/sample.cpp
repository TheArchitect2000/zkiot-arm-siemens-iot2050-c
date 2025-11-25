// sample.cpp
#include <cstdint>
#include <cstdio>

volatile uint64_t sink;

int main() {
    uint64_t a = 5, b = 7, c = 2;

    uint64_t s1 = a + b;          // add
    uint64_t s2 = s1 - c;         // sub
    uint64_t p  = s2 * c;         // mul
    uint64_t aa = (a & b);        // and
    uint64_t oo = (a | b);        // orr

    uint64_t sh = (b << 1) | ((c >> 1) & 0xF);

    sink = s1 ^ s2 ^ p ^ aa ^ oo ^ sh;
    std::printf("%llu\n", (unsigned long long)sink);
    return 0;
}
