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

int main()
{
  init();
  char buf[40];
  unsigned int key;
  unsigned guess;
  memset(buf, 0, 40);
  srand(time(0));
  key = rand();
  read(0, buf, 32);
  printf(buf);
  scanf("%d", &guess);
  if (guess == key)
    bbbaaaccckkkddd000ooorrr();
  return 0;
}
