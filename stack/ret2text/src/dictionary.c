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
    size_t tmp;
    size_t var_to_override = 0xdeadbeaf;
    char buf[32];
    puts("var before gets :");
    printf("0x%lx\n", var_to_override);
    puts("Now input something :");
    gets(buf);
    puts("var after gets :");
    printf("0x%lx\n", var_to_override);
    return 0;
}


void bbbaaaccckkkddd000ooorrr()
{
    puts("successful");
    asm("push 0x601020");
    system("/bin/sh\x00");
}

