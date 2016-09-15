#include <iostream>
#include <string>

using namespace std;

int main() {
	int table[5][2] = { { 1, 2 }, { 1, 3 }, { 4, 2 }, { 4, 4 }, {4, 4} };
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
			if (state == 2 || state == 3) {
				cout << w << " is accepted. \n";
			}
			else{
				cout << "Not accepted\n";
			}
			
		}
		else {
			cout << "Not accepted\n";
			break;
		}
		state = table[state][col];
	}

	return 0;
}