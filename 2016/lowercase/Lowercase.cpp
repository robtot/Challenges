#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main (int argc, char **argv)
{
	ifstream input (argv[1]);
	string line;

	if (input.is_open())
	{
		while (getline(input, line))
		{
			for (string::size_type i=0; i<line.length(); ++i)
			{
				cout<<(char)tolower(line[i]);
			}
			cout<<endl;
		}
	}
	else
	{
		cout<<"No file arg!"<<endl;
	}
	return 0;
}
