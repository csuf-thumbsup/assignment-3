#include <fstream>
#include <string>
#include <iostream>
#include <sstream>
#include <algorithm>

using namespace std;

void removeComments(string &str)
{
	int endpos = str.find_first_of('//');
	if (string::npos != endpos)
	{
		str = str.substr(0, endpos);
	}
}

void trim(string &str)
{
	// trim leading spaces
	size_t startpos = str.find_first_not_of(" \t");
	if (string::npos != startpos)
	{
		str = str.substr(startpos);
	}

	// trim trailing spaces
	size_t endpos = str.find_last_not_of(" \t");
	if (string::npos != endpos)
	{
		str = str.substr(0, endpos + 1);
	}
}

string getData()
{
	fstream fs("data.txt");
	string line, result;
	while (getline(fs, line))
	{
		// pre checks
		//cout << line << endl;
		// skip line if it starts with a comment "\\"
		if (line[0] == '\/' && line[1] == '\/')
		{
			continue;
		}
		else if (line.empty())
		{
			continue;
		}
		else 
		{
			// filter out comments in line 
			removeComments(line);

			//trim trailing whitespaces from line
			trim(line);

			result += line ;
		}
	}
	return result;
}

bool is_terminal(char ch)
{
	if (ch == ',' || ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '=')
		return true;
	return false;
}

bool bothAreSpaces(char lhs, char rhs) 
{
	return (lhs == rhs) && (lhs == ' '); 
}

void removeMultiSpaces(string &str)
{
	string::iterator new_end = unique(str.begin(), str.end(), bothAreSpaces);
	str.erase(new_end, str.end());
}

string processData(string data)
{
	string result, temp;
	stringstream ss;
	bool space_used = false;

	// semi-format string 
	for (int i = 0; i < data.size(); i++)
	{
		if (!isspace(data[i]))
		{
			//special case for semicolons
			if (data[i] == ';')
			{
				result += ' ';
				result += data[i];
				result += '\n';
			}
			else if (is_terminal(data[i]))
			{
				result += ' ';
				result += data[i];
				result += ' ';
			}
			else
			{
				result += data[i];
			}
			//reset space_used flag
			space_used = false;
		}
		else
		{
			if (!space_used)
			{
				// only add one space
				result += ' ';
				space_used = true;
			}
		}
	}

	ss.str(result); // store semi-formatted string into ss
	result.clear(); // clear out content to reuse

	while (!ss.eof())
	{
		// beautifying each line 
		getline(ss, temp);
		trim(temp);
		removeMultiSpaces(temp);
		result += temp + '\n';
	}

	return result;
}

void saveData(string data)
{
	ofstream fs("newdata.txt");
	fs << data;
}

int main()
{
	string result = processData(getData());
	saveData(result);
}