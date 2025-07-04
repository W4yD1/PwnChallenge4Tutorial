#include <stdio.h>
#include <string.h>

char flag[100];

void init()
{
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);

    int fd = open("/flag", 0, 0);
    read(fd, flag, 100);
    close(fd);
}

void vuln()
{
    char buf[32];
    puts("trigger stack smash");
    gets(buf);
}

int main()
{
    init();
    vuln();
    return 0;
}
