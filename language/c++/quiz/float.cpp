#include <iostream>

using namespace std;

int main()
{
    float x = 0.00001;
    if (x == 0.00001)
    {
        cout << "Hello World" << endl;
    }
    else
    {
        cout << x << endl;
    }
    
    float y = 0.00000;
    if (y == 0.00000)
    {
        cout << "Hello World" << endl;
    }
    else
    {
        cout << y << endl;
    }

    return 0;
}
/*
 * 运行结果
 */

// result
// 1e-05
// Hello World
// ？w问点， 如何比较浮点数是否相同