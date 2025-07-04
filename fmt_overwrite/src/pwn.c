#include <stdio.h>
#include <string.h>

unsigned long key = 0;

void init()
{
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
}

void bbbaaaccckkkddd000ooorrr()
{
    system("/bin/sh\x00");
}

int main()
{
    init();
    char buf[40];
    unsigned long *keyptr = &key;
    memset(buf, 0, 40);
    read(0, buf, 32);
    printf(buf);
    if (key == 0xbeef)
        bbbaaaccckkkddd000ooorrr();
    return 0;
}
