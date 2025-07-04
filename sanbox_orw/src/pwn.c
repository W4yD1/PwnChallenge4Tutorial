#include <stdio.h>
#include <string.h>
#include <seccomp.h>
#include <linux/seccomp.h>

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

void sanbox()
{
    scmp_filter_ctx ctx;
    ctx = seccomp_init(SCMP_ACT_ALLOW);

    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execve), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execveat), 0);
    seccomp_load(ctx);
}

char code[0x100];

int main()
{
    init();
    sanbox();
    puts("Input something :");
    mprotect((long)code & 0xfffffffff000, 0x1000, 7);
    read(0, code, 0x100);
    sanbox();
    (*(void (*)())code)();
    return 0;
}
