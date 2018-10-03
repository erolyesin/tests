#include <stdio.h> 

int main(void)
{
    // while (printf("Hello World ")) 
    // ;
    unsigned number = 4;
    int count = 0;

    while (number)
    {
        number = (unsigned)number >> 1;
        if (number)
            count++;
        printf ( "count: %d - number: %d\n", count, (unsigned)number);
   }
    printf ( "bit count: %d\n", count);
}
