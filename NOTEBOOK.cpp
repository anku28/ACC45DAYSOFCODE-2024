#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;  // Number of test cases
    
    while (T--) {
        int N;
        cin >> N;  // Weight of pulp in kg
        cout << N * 10 << endl;  // Each kg of pulp makes 10 notebooks
    }
    
    return 0;
}