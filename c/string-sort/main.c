#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int is_bigger( char *str1,  char *str2)
{
    char *pstr1 = str1;
    char *pstr2 = str2;

    while (*pstr1 && *pstr2)
    {
        if (*pstr1 > *pstr2 )
        {
            return 1;
        }
    }
    if ( *pstr1 && !*pstr2 )
        return 1;
    return 0;
}

void sort_words(char *words[], int count)
{
    
}

#ifndef RunTests
int main()
{
    char *words[] = { "cherry", "orange", "apple" };

    sort_words(words, 3);

    for (int i = 0; i < 3; i++)
    {
        printf("%s ", words[i]);
    }
}
#endif
