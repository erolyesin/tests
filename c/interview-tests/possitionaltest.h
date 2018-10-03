//
//  possitionaltest.h
//  test2
//
//  Created by Erol Yesin on 2018.08.30.
//  Copyright © 2018 CasaYesin. All rights reserved.
//

#ifndef possitionaltest_h
#define possitionaltest_h

#include <stdio.h>

typedef struct
{
    double x;
    double y;
} point;

typedef struct
{
    double     slope;
    double     intersect;
    point    vertx[2];
}line;

extern double slope( point *vertx1, point *vertx2 );
extern int slope_intersect( line *segment );
extern point *intersect( line *target, line *segment );
extern int x_is_within( double x, line *target, line *segment );
extern int y_is_within( double y, line *target, line *segment );

#endif /* possitionaltest_h */
