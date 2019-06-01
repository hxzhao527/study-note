#include <iostream>

int main()
{
    auto x = [](int x) { return x; };
    decltype(x) *a;

    std::cout << sizeof(*a);
}

/*
 * 是否可编译通过，如果编译通过，给出运行结果
 */

// result
// 1