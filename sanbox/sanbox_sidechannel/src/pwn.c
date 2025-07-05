#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <sys/prctl.h>
#include <linux/filter.h>
#include "seccomp-bpf.h"

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

int sanbox()
{
    struct sock_filter filter[] = {
        /* Validate architecture. */
        VALIDATE_ARCHITECTURE,
        /* Grab the system call number. */
        EXAMINE_SYSCALL,
        BLOCK_SYSCALL(execve),
        BLOCK_SYSCALL(execveat),
        BLOCK_SYSCALL(write),
        BLOCK_SYSCALL(writev),
        ALLOW_PROCESS,
    };
    struct sock_fprog prog = {
        .len = (unsigned short)(sizeof(filter) / sizeof(filter[0])),
        .filter = filter,
    };

    if (prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0))
    {
        perror("prctl(NO_NEW_PRIVS)");
        goto failed;
    }
    if (prctl(PR_SET_SECCOMP, SECCOMP_MODE_FILTER, &prog))
    {
        perror("prctl(SECCOMP)");
        goto failed;
    }
    return 0;

failed:
    if (errno == EINVAL)
        fprintf(stderr, "SECCOMP_FILTER is not available. :(n");
    return 1;
}

char code[0x100];

int main()
{
    init();
    puts("Input something :");
    mprotect((long)code & 0xfffffffff000, 0x1000, 7);
    read(0, code, 0x1000);
    sanbox();
    (*(void (*)())code)();
    puts("bye!");
    return 0;
}
