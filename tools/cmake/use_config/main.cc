#include "config.h"
#include <cstdio>

int main()
{
    std::printf("%s(%d.%d) is is built on %s by %s", PROJECT_NAME,
                PROJECT_VERSION_MAJOR, PROJECT_VERSION_MINOR,
                HOST_OS_NAME, AUTHOR);
    return 0;
}