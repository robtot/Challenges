#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main (int argc, char **argv)
{
	ifstream inputFile { argv[1] };
	string inputLine {};

	while (getline(inputFile, inputLine))
	{	
		char searchCharacter {inputLine.back()};
		inputLine.pop_back();
		size_t characterPosition {inputLine.find_last_of(searchCharacter)};

		if (characterPosition == string::npos)
			cout<<"-1"<<endl;
		else
			cout<<characterPosition<<endl;
	}

	return 0;
}
