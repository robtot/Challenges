#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int getFibonacci(int x)
{
	if (x==1)
	{
		return 1;
	}
	else if (x==0)
	{
		return 0;
	}
	return getFibonacci(x-1)+getFibonacci(x-2);
}

int main (int argc, char **argv)
{
	ifstream input {argv[1]};
	string line {""};

	while (getline(input, line))
	{
		cout<<getFibonacci(stoi(line))<<endl;
	}
	return 0;
}

