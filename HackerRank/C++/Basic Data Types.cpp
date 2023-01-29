#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int x; long y; char c; float f; double z;
    cin >> x >> y >> c >> f >> z ;
    cout << x << "\n" << y << "\n" << c << "\n";
    printf("%.3f\n", f); 
    printf("%.9lf", z);
    
    return 0;
}
