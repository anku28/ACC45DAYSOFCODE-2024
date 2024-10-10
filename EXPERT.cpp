#include <iostream>
using namespace std;

int main() {
    int T;  // Number of test cases
    cin >> T;

    while (T--) {
        int X, Y;
        cin >> X >> Y;

        // Check if Y is at least 50% of X
        if (Y * 2 >= X) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }

    return 0;
}
