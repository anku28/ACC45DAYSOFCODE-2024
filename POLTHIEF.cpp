#include <iostream>
#include <cmath>  // for abs()
using namespace std;

int main() {
    int T;  // Number of test cases
    cin >> T;

    while (T--) {
        int X, Y;
        cin >> X >> Y;

        // The time is the absolute difference between X and Y
        int time = abs(X - Y);
        cout << time << endl;
    }

    return 0;
}