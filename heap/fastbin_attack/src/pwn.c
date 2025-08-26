#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void init()
{
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
}

void win()
{
    puts("Congratulations! You successfully exploited the fast bin!");
    system("/bin/sh");
}

void print_menu()
{
    puts("=== Fast Bin Attack Challenge ===");
    puts("1. Allocate chunk");
    puts("2. Free chunk");
    puts("3. Edit chunk");
    puts("4. Show chunk");
    puts("5. Exit");
    printf("Choice: ");
}

struct chunk_info {
    void* ptr;
    size_t size;
    int in_use;
};

struct chunk_info chunks[10];
int chunk_count = 0;

int main()
{
    init();
    int choice;
    int idx;
    size_t size;
    
    puts("Welcome to the Fast Bin Attack challenge!");
    puts("Try to get a shell by exploiting the fast bin mechanism.");
    printf("win function is at: %p\n", win);
    
    while (1) {
        print_menu();
        scanf("%d", &choice);
        
        switch (choice) {
            case 1: // Allocate
                if (chunk_count >= 10) {
                    puts("Too many chunks!");
                    break;
                }
                printf("Size: ");
                scanf("%ld", &size);
                if (size > 0x80) {
                    puts("Size too large!");
                    break;
                }
                chunks[chunk_count].ptr = malloc(size);
                chunks[chunk_count].size = size;
                chunks[chunk_count].in_use = 1;
                printf("Allocated chunk %d at %p\n", chunk_count, chunks[chunk_count].ptr);
                chunk_count++;
                break;
                
            case 2: // Free
                printf("Index: ");
                scanf("%d", &idx);
                if (idx < 0 || idx >= chunk_count || !chunks[idx].in_use) {
                    puts("Invalid index!");
                    break;
                }
                free(chunks[idx].ptr);
                chunks[idx].in_use = 0;
                printf("Freed chunk %d\n", idx);
                break;
                
            case 3: // Edit
                printf("Index: ");
                scanf("%d", &idx);
                if (idx < 0 || idx >= chunk_count) {
                    puts("Invalid index!");
                    break;
                }
                printf("Data: ");
                read(0, chunks[idx].ptr, chunks[idx].size);
                puts("Chunk edited!");
                break;
                
            case 4: // Show
                printf("Index: ");
                scanf("%d", &idx);
                if (idx < 0 || idx >= chunk_count || !chunks[idx].in_use) {
                    puts("Invalid index!");
                    break;
                }
                printf("Chunk %d: ", idx);
                write(1, chunks[idx].ptr, chunks[idx].size);
                puts("");
                break;
                
            case 5: // Exit
                puts("Goodbye!");
                exit(0);
                
            default:
                puts("Invalid choice!");
        }
    }
    
    return 0;
}