#include <stdio.h>

// char code[] = "\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05";

void init()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}
char code[0x100];

int main()
{
    init();
    char buf[32] = "Shellcode: ";
    puts(buf);
    mprotect((long)code & 0xfffffffff000, 0x1000, 7);
    read(0, code, 10);
    (*(void (*)())code)();
    return 0;
}

