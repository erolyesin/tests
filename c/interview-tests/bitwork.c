//
//  bitwork.c
//  test2
//
//  Created by Erol Yesin on 2018.08.30.
//  Copyright © 2018 CasaYesin. All rights reserved.
//

#include "bitwork.h"

enum { BITS_PER_LONG = sizeof(long) * 8 };
#define LONG_OFFSET(b) ((b) / BITS_PER_LONG)
#define BIT_OFFSET(b)  ((b) % BITS_PER_LONG)

void set_bit(long *words, int n)
{
    words[LONG_OFFSET(n)] |= (1 << BIT_OFFSET(n));
}

void clear_bit(long *words, int n)
{
    words[LONG_OFFSET(n)] &= ~(1 << BIT_OFFSET(n));
}

int get_bit( long *words, int n)
{
    int bit = words[LONG_OFFSET(n)] & (1 << BIT_OFFSET(n));
    return bit != 0;
}

int bit_count( long word )
{
    int count = 0;
    while ( word )
    {
        count++;
        word &= (word - 1);
    }
    return count;
}
