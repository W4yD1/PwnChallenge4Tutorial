#include <stdio.h>
#include <string.h>

void init()
{
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
}



int main()
{
    init();
    char buf[32];
    puts("Now input something :");
    read(0, buf, 48);
    return 0;
}
