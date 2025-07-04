#include <stdio.h>
#include <string.h>

void init()
{
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
}

void vuln()
{
    char buf[32];
    puts("input:");
    read(0, buf, 0x100);
}

void backdoor()
{
    system("/bin/sh\x00");
}

int main()
{
    int pid;
    init();
    while (1)
    {
        pid = fork();
        if (pid)
        {
            wait(0);
        }
        else
        {
            vuln();
            break;
        }
    }
    return 0;
}

