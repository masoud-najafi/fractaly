#include <stdio.h>

#if defined _WIN32 || defined __CYGWIN__
/* Note: both gcc & MSVC on Windows support this syntax. */
#define MY_Export __declspec(dllexport)
#else
#if __GNUC__ >= 4
#define MY_Export __attribute__ ((visibility ("default")))
#else
#define MY_Export
#endif
#endif


MY_Export int adder(int a, int b) {  // only adder is exported for Win64 and Linux64
    return a+b;
}
 
 int product(int a, int b) {
    return a *b;
}

// cl /LD /Fefractal_maths.dll fractal_maths.c /link /EXPORT:adder
// gcc -fPIC -shared -o libfractal_maths.so fractal_maths.c  -fvisibility=hidden