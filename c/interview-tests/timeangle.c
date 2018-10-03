//
//  timeangle.c
//  test2
//
//  Created by Erol Yesin on 2018.08.30.
//  Copyright © 2018 CasaYesin. All rights reserved.
//

#include <math.h>
#include "timeangle.h"

float diffMinHrAngle( int hour, int minute )
{
    float delta = fabs( 30.0*(hour%12) - 5.5*(minute%60) );
    float min_delta = delta<=180.0 ? delta : (360 - delta);
    return min_delta;
}

// int hour_angle = h*30 + m*0.5;
// int minute_angle = 6*m;
// h*30 + m*0.5 = 6*m
// h*30 = 6*m - m*0.5 = m*5.5
// m = h * 30/5.5
// h = m * 5.5 / 30

float overlayMin( int hour )
{
    float min;
    min = (hour%12) * 30.0 / 5.5;
    return min;
}

int overlayHour( int min )
{
    int hour;
    hour = (min%60) * 5.5 / 30.0;
    return hour%12;
}
