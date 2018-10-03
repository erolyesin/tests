#include <stdlib.h>
#include <stdio.h>

int inspect_bits(unsigned int number)
{
    if ( number & (number<<1))
        return 1;
    return 0;
}

#ifndef RunTests
int main ()
{
    printf("%d\n", inspect_bits(5));
}
#endif
