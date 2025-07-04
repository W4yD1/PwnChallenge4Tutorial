#include <stdio.h>
#include <unistd.h>

void init()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

char binsh[32] = "/bin/sh";

void gift()
{
    asm("syscall; popq %rdx; ret; popq %rax; ret");
}

int main()
{
    init();
    char buf[32] = "syscall is amazing";
    puts(buf);
    read(0, buf, 0x100);
    return 0;
}
