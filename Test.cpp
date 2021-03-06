#include <iostream>
#include <string>
#include <fstream>

using namespace std;

void check_word(string w)
{
    int table[5][2] = { { 1, 2 }, { 1, 3 }, { 4, 2 }, { 4, 4 }, {4, 4} };
	int state = 0;
	int col;
	
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
				cout << w << " is not accepted\n";
			}
		
		}
		else {
			cout << w << " is not accepted\n";
			break;
		}
		state = table[state][col];
	}
}


int main() {
	string w;
	fstream file;

	file.open("data.txt");
	
	do {

		file >> w;
		check_word(w);
		cout << endl;
	} while (!file.eof());

	

	file.close();
	return 0;
}
