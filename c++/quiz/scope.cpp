#include <iostream>
static int x = 5;
int main(int argc, char **argv)
{
    int x = x;
    std::cout << x;
    return 0;
}
/*
 * 是否可编译通过，如果编译通过，给出运行结果
 */

// result
// 0 （需要看编译器版本)