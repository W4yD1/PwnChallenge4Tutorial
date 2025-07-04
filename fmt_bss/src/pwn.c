#include <stdio.h>
#include <string.h>

char buf[40];

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

int game()
{
    int i;
    for (i = 0; i < 3; i++)
    {
        memset(buf, 0, 40);
        read(0, buf, 40);
        printf(buf);
    }
    return 0;
}

int main()
{
    init();
    game();
    return 0;
}
