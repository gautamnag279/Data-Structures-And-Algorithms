#include <iostream>
using namespace std;

int main() {
    int i = 0;
    int sum = 0;
    
    while (cin >> i) {
        sum += i;
    }
    
    cout << sum << endl;
    
    return 0;
}
