#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int is_palindrome(char *str)
{
    int end = (int)strlen(str) - 1;
    int bgn = 0;

    if ( end == -1 )
        return 0;
    while (bgn < end)
    {
        char end_c = str[end];
        char bgn_c = str[bgn];
        if (bgn_c < 'a' )
            bgn_c += 'a' - 'A';
        if (end_c < 'a' )
            end_c += 'a' - 'A';
        if (bgn_c != end_c)
            return 0;
        bgn++;
        end--;
    }

    return 1;
}

#ifndef RunTests
int main()
{
    char *str = "Dleveled";
    printf("%d\n", is_palindrome(str));
}
#endif
