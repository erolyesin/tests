//
//  strtests.h
//  test2
//
//  Created by Erol Yesin on 2018.08.30.
//  Copyright © 2018 CasaYesin. All rights reserved.
//

#ifndef strtests_h
#define strtests_h

#include <stdio.h>

extern int stoi(const char *str, int *err );
extern int find_char_offset( char *str, char ch );
extern char *reverse_string( char *str );

extern char *strarr[];

#endif /* strtests_h */
