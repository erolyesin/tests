//
//  bitwork.h
//  test2
//
//  Created by Erol Yesin on 2018.08.30.
//  Copyright © 2018 CasaYesin. All rights reserved.
//

#ifndef bitwork_h
#define bitwork_h

#include <stdio.h>

extern void set_bit(long *words, int n);
extern int get_bit(long *words, int n);
extern void clear_bit(long *words, int n);
extern int bit_count( long word );

#endif /* bitwork_h */
