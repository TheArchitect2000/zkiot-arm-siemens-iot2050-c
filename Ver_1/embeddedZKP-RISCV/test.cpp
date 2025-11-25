// #include "polynomial.h"
// #include <iostream>
// #include <fstream>
// #include <string>

// using namespace std;

// int main() {
//     uint64_t R2 = 7;
//     uint64_t R3 = 5;

//     uint64_t R5 = 0;
//     uint64_t p = 5087281;

//     uint64_t R1 = (R2 * (Polynomial::pInverse(R3, p))) % p;
//     R5 = ((R2 % R3) * (Polynomial::pInverse(R3, p))) % p;
//     R5 = (R5 * (p-1)) % p;
//     R1 = (R1 + R5) % p;


//     uint64_t r1 = (R2 / R3) % p;
//     cout << "PC: " << r1 << endl;

//     cout << "ZKP: " << R1 << endl;

//     return 0;
// }