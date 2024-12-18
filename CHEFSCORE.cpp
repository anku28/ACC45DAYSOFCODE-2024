#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T; // Number of test cases
    
    while (T--) {
        int N, X, Y;
        cin >> N >> X >> Y; // Number of problems, marks per problem, and desired score
        
        // Check if Y can be achieved
        if (Y <= N * X && Y % X == 0) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    
    return 0;
}
