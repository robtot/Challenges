#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main (int argc, char **argv)
{
	ifstream input {argv[1]};
	int sum = 0;
	for (string line; getline(input, line);)
	{
		sum+=stoi(line);
	}
	cout<<sum<<endl;
	return 0;
}
