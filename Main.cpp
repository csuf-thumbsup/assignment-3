#include <iostream>
#include <string>

using namespace std;

int main() {
	int table[4][2] = { { 1, 2 }, { 1, 2 }, { 3, 2 }, {3, 3} };
	int state = 0;
	int col;
	string w;

	cout << "Enter a string that ends with $: ";
	cin >> w;

	for (int i = 0; i < w.length(); i++) {
		if (w[i] == 'a') {
			col = 0;
		}
		else if (w[i] == 'b') {
			col = 1;
		}
		else if (w[i] == '$') {
			cout << w << " is accepted. \n";
		}
		else {
			cout << "Not accepted\n";
			break;
		}
		state = table[state][col];
	}
	
	return 0;
}