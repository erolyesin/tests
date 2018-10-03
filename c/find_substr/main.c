//
//  main.c
//  find_substr
//
//  Created by Erol Yesin on 2018.09.23.
//  Copyright © 2018 CasaYesin. All rights reserved.
//

#include <stdio.h>
#include <string.h>
#include <math.h>

#define MAX(_x,_y)  ((_x)<(_y)?(_y):(_x))
#define OFFSET(_s,_c) ((strchr((_s),(_c)))?(strchr((_s),(_c)))-(_s):NULL)

void foo(char* input, int shift)
{
    int count = (int)strlen(input);
    while (input && count--)
        printf("%c", (input++)[0]+shift);
}

void test_foo(int shift_min, int shift_max)
{
    char *str_arr[] =
    {
        "I KNOW IT",
        "A NEW YEAR",
        "A NEW DAY",
        "A BIG CAT"
    };
    for ( int shift=shift_min; shift<=shift_max; shift++)
    {
        printf("\nindx=%d", shift);
        for (int indx=0; indx<4; indx++)
        {
            printf("\n%s:[%d]:", str_arr[indx], shift);
            foo(str_arr[indx], shift);
        }
    }
    puts("");
}

// https://leetcode.com/articles/longest-substring-without-repeating-characters/
int lengthOfLongestSubstring(char* str)
{
    int size = (int)strlen(str);
    int max_sz = 0;
    int hist[128]; // current index of character
    memset(hist, 0, sizeof(hist));
    int win_head = 0;
    int max_head = 0;

    for (int here = 0; here < size; here++)
    {
//        printf("[i]i=%d, j=%d, ans=%d, index[%c(%d)]=%d\n",
//               win_head, here, max_sz, str[here], (int)str[here], hist[str[here]]);
        win_head = MAX(hist[str[here]], win_head);
        if ( max_sz < (here - win_head + 1) )
        {
            max_sz = MAX(max_sz, (here - win_head + 1) );
            max_head = win_head;
        }
        hist[str[here]] = here + 1;
//        printf("[o]i=%d,      ans=%d, index[%c(%d)]=%d\n",
//               win_head, max_sz, str[here], (int)str[here], hist[str[here]]);
    }
    printf("longest substr = \"%.*s\"\n", max_sz, &str[max_head] );
    return max_sz;
}

double funct1(double n)
{
    double result = n;
    for(int i=0; i<10000; ++i)
        result /= log(n);
    return result;
}
double funct2(double n)
{
    int i = 0;
    double orig_n = n;
    while (++i < 10000)
        n = n/log(orig_n);
    return n;
}
double funct3(double n)
{
    double log_n = log(n);
    for(int i=0; i<10000; ++i)
        n = n/log_n;
    return n;
}

int main()
{
//    char str[] = "Hello, World! Welcome to My Reality...";  // insert code here...
//    printf( "%s\n", str);
//    int ans = lengthOfLongestSubstring(str);
//    printf( "lengthOfLongestSubstring: %d\n", ans);
//    puts("\n\n");

//    test_foo(10, 10);

    double n = 8577466389642568;
    printf("func1(%0.3f)=%0.3f\n", n, funct1(n));
    printf("func2(%0.3f)=%0.3f\n", n, funct2(n));
    printf("func3(%0.3f)=%0.3f\n", n, log(n));
    return 0;
}
