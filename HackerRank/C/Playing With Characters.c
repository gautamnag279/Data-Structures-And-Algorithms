#include <stdio.h>

int main()
{
    char a[100],b[100],s[100];
    scanf("%s\n%s\n%[^\n]%*c",&a,&b,s); 
    printf("%s\n%s\n%s",a,b,s);
return 0;
}
