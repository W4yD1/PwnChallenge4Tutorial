#include <stdio.h>
#include <string.h>

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

void vuln()
{
    char buf[32];
    size_t target;
    puts("where do you wanna read");
    read(0, &target, 8);
    puts("your content");
    read(0, target, 8);

    puts("trigger stack smash");
    read(0, buf, 0x100);
}

int main()
{
    init();
    vuln();
    return 0;
}
