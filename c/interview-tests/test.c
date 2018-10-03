/*
 ============================================================================
 Name        : test.c
 Author      : Erol Yesin
 Version     : v0.0.1
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "bitwork.h"
#include "timeangle.h"
#include "strtests.h"
#include "possitionaltest.h"

int main(void)
{
    line lines[2] =
    {
        { 0, 0, {{20.0,10.0}, {10,20}}},
        { 0, 0, {{10.0,5.0}, {15.0,25.0}}}
    };

    char str_num[] = "-111";
    time_t _time = time(NULL);
    struct tm *tm_struct = localtime( &_time );
    int err = 0;

    printf( "time:%02d:%02d:angle:%0.2f degrees:\n",
           tm_struct->tm_hour, tm_struct->tm_min,
           diffMinHrAngle( tm_struct->tm_hour, tm_struct->tm_min ) );

    printf( "%s:%d:err:%d\n", str_num, stoi(str_num, &err ), err);

    {
        long number = 1152939097070309376;
        int offset = 19;

        printf( "bit:%d:%d:%d bits\n", offset, get_bit( &number, offset ), bit_count( number ));
        clear_bit( &number, offset );
        printf( "bit:%d:%d:%d bits\n", offset, get_bit( &number, offset ), bit_count( number ));

        for ( offset = 0; strarr[offset]; offset++ )
        {
            printf( "%s -> ", strarr[offset] );
            puts( reverse_string( strarr[offset] ) );
        }
    }
    slope_intersect( &lines[0] );
    slope_intersect( &lines[1] );
    {
        point *cross = intersect( &lines[0], &lines[1] );
        if ( cross != NULL )
        {
            if ( x_is_within( cross->x, &lines[0], &lines[1] )
                && y_is_within( cross->x, &lines[0], &lines[1] ) )
            {
                puts( "lines intersect");
            }
            else
            {
                puts( "lines don't intersect");
            }
        }
        else
        {
            puts( "lines don't intersect");
        }
    }

    return EXIT_SUCCESS;
}
