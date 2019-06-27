#include <cstdio>
#include <zlib.h>
#include <libavformat/avformat.h>

int main()
{
    std::printf("using version %s of zlib", zlibVersion());
    return 0;
}