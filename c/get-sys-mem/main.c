//
//  main.c
//  test2
//
//  Created by Erol Yesin on 2018.09.15.
//  Copyright © 2018 CasaYesin. All rights reserved.
//

#include <stdio.h>
#include <unistd.h>
#include <math.h>
#define SQR(x) (x)*(x)

unsigned long long getTotalSystemMemory()
{
    long pages = sysconf(_SC_PHYS_PAGES);
    long page_size = sysconf(_SC_PAGE_SIZE);
    return pages * page_size;
}

int main(int argc, const char * argv[]) {
    int N = 55;
//    int s = SQR(5+1);
//    printf("%d\n", s);
    printf("Total mem: %llu\n", getTotalSystemMemory());
    printf("For %d decimal digit number you need %0.0f-bit variable\n",
           N, (ceil((N/log10(2))/8)+1)*8);

    puts("");
    return 0;
}
