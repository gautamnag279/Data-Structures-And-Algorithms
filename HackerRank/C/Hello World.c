int main() 
{
    char s[100];
    // %[^\n]%*c is used to take a line as an input rather than a string
    scanf("%[^\n]%*c", s);
    printf("Hello, World!\n%s", s);   
    return 0;
}
