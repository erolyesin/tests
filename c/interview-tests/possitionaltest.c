//
//  possitionaltest.c
//  test2
//
//  Created by Erol Yesin on 2018.08.30.
//  Copyright © 2018 CasaYesin. All rights reserved.
//

#include "possitionaltest.h"

double slope( point *vertx1, point *vertx2 )
{
    double d_x = (vertx1->x - vertx2->x);
    double d_y = (vertx1->y - vertx2->y);
    if ( d_x == 0 )
    {
        return 0.0;
    }
    return d_y / d_x;
}

int slope_intersect( line *segment )
{
    if ( segment == NULL )
    {
        return -1;
    }
    segment->slope = slope( &segment->vertx[0], &segment->vertx[1]);
    if ( segment->slope == 0.0 || segment->vertx[0].x == 0.0 )
    {
        return -1;
    }
    segment->intersect = segment->vertx[0].y - (segment->slope*segment->vertx[0].x);
    return 0;
}

point *intersect( line *target, line *segment )
{
    // y = m*x + k
    // x1 = x2 => m1*x + k1 = m2*x + k2
    // x = (k2 - k1) / (m1 - m2)
    static point cross;
    double d_slope = target->slope - segment->slope;
    // if the slopes are the same, lines do not intersect
    if ( d_slope == 0.0 || target->slope == -segment->slope )
    {
        return NULL;
    }
    cross.x = ( segment->intersect - target->intersect ) / d_slope;
    cross.y = segment->slope*cross.x + segment->intersect;
    return &cross;
}

int x_is_within( double x, line *target, line *segment )
{
    double min = segment->vertx[0].x < segment->vertx[1].x ? segment->vertx[0].x : segment->vertx[1].x;
    double max = min == segment->vertx[0].x? segment->vertx[1].x : segment->vertx[0].x;
    int within_segment = ( min <= x && x <= max );
    int within_target = 0;

    min = target->vertx[0].x < target->vertx[1].x ? target->vertx[0].x : target->vertx[1].x;
    max = min == target->vertx[0].x? target->vertx[1].x : target->vertx[0].x;
    within_target = ( min <= x && x <= max );

    return within_segment && within_target;
}

int y_is_within( double y, line *target, line *segment )
{
    double min = segment->vertx[0].y < segment->vertx[1].y ? segment->vertx[0].y : segment->vertx[1].y;
    double max = min == segment->vertx[0].y? segment->vertx[1].y : segment->vertx[0].y;
    int within_segment = ( min <= y && y <= max );
    int within_target = 0;

    min = target->vertx[0].y < target->vertx[1].y ? target->vertx[0].y : target->vertx[1].y;
    max = min == target->vertx[0].y? target->vertx[1].y : target->vertx[0].y;
    within_target = ( min <= y && y <= max );

    return within_segment && within_target;
}
