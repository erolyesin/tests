//
//  strtests.c
//  test2
//
//  Created by Erol Yesin on 2018.08.30.
//  Copyright © 2018 CasaYesin. All rights reserved.
//

#include "strtests.h"

char str1[] = "I like to build";
char str2[] = "I am Erol";
char str3[] = "12345";
char *strarr[] =
{
    str1,
    str2,
    str3,
    NULL
};

int stoi(const char *str, int *err )
{
    char *nxt = ( *str == '-' || *str == '+' ) ? &str[1] : str;
    int sum = 0;

    while (*nxt)
    {
        if ( *nxt > '9' || *nxt < '0' )
        {
            *err = -1;
            return 0;
        }
        sum = (sum*10) + *nxt - '0';
        nxt++;
    }

    return *str == '-' ? -sum : sum;
}

int find_char_offset( char *str, char ch )
{
    int offset = 0;
    char *ptr = str;
    if ( str == NULL || *str == '\0' )
    {
        return -1;
    }

    while ( *ptr != ch && *ptr != '\0' )
    {
        offset++;
        ptr++;
    }
    return offset;
}

char *reverse_string( char *str )
{
    int beg = 0;
    int str_size = find_char_offset( &str[beg], '\0' );

    for ( beg = 0; beg < str_size; beg++ )
    {
        int word_size = find_char_offset( &str[beg], ' ' );

        if ( word_size < 0 )
            break;

        if ( word_size <= 1 )
        {
            beg++;
        }
        else
        {
            int word_end = beg + word_size;
            int end;

            for ( end = word_end - 1; beg < end; end-- )
            {
                char buf = str[beg];
                str[beg] = str[end];
                str[end] = buf;
                beg++;
            }
            beg = word_end;
        }
    }
    return str;
}
