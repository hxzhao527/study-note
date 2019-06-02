#include <cstdio>

#ifdef USE_MYMATH
#include "fmath.h"
#else
#include <cmath>
using std::pow;
#endif

int main()
{
    std::printf("pow(%f, %d) = %f", 2.0, 2, pow(2.0, 2));
    return 0;
}