#include <iostream>
const int x = 5;
int main(int argc, char **argv)
{
    int x[x];

    int y = sizeof(x) / sizeof(int);
    std::cout << y;
    return 0;
}
/*
 * 是否可编译通过，如果编译通过，给出运行结果
 */

// result
// 5