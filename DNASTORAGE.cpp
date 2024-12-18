#include <iostream>
#include <unordered_map>
using namespace std;

// Function to encode binary string to DNA sequence
string encodeDNA(const string& binaryStr) {
    unordered_map<string, char> encodingMap = {
        {"00", 'A'},
        {"01", 'T'},
        {"10", 'C'},
        {"11", 'G'}
    };
    string result;
    for (size_t i = 0; i < binaryStr.length(); i += 2) {
        string pair = binaryStr.substr(i, 2);
        result += encodingMap[pair];
    }
    return result;
}

int main() {
    int T;
    cin >> T; // Number of test cases
    while (T--) {
        int N;
        cin >> N; // Length of the binary string
        string binaryStr;
        cin >> binaryStr;
        cout << encodeDNA(binaryStr) << endl;
    }
    return 0;
}
