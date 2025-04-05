#include <stdio.h>
__declspec(dllexport) int adder(int a, int b) {
    return a+b;
}
 
__declspec(dllexport) int product(int a, int b) {
    return a *b;
}

// cl /LD /Fefractal_maths.dll fractal_maths.c /link /EXPORT:adder
// gcc -shared -o fractal_maths.dll fractal_maths.c -Wl,--export-all-symbols