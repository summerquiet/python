#include <stdio.h>

void main(void)
{
    char a[] = "OK^GSYBEX^Y";
    printf(a);
    printf("\n");

    int n = strlen(a);
    memfrob(a,n);
    printf(a);
    printf("\n");

    memfrob(a,n);
    printf(a);
    printf("\n");

    return 0;
}
