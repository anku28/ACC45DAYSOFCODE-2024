#include <iostream>
using namespace std;

int main() {
    int T;  // Number of test cases
    cin >> T;

    while (T--) {
        int N, A, B;  // Number of episodes, duration of even-indexed, and odd-indexed episodes
        cin >> N >> A >> B;

        // Calculate the count of odd-indexed and even-indexed episodes
        int oddCount = (N + 1) / 2;   // Odd-indexed episodes
        int evenCount = N / 2;        // Even-indexed episodes

        // Calculate the total duration
        int totalDuration = oddCount * B + evenCount * A;

        cout << totalDuration << endl;
    }

    return 0;
}
