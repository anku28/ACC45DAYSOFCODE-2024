#include <iostream>
using namespace std;

int main() {
    int T;  // Number of test cases
    cin >> T;

    while (T--) {
        int X, Y;
        cin >> X >> Y;

        if (X >= Y) {
            // If renting for even 1 month costs more or the same as buying, output 0
            cout << 0 << endl;
        } else {
            // Calculate the maximum months Chef can rent such that rent cost is strictly less than buying
            int max_months = (Y - 1) / X;
            cout << max_months << endl;
        }
    }

    return 0;
}