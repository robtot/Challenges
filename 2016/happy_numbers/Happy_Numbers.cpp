#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int squared(int number)
{
	return number*number;
}


int main(int argc, char **argv)
{
	ifstream input {argv[1]};
	string lineNumber {};
	while (getline(input,lineNumber))
	{
		if (lineNumber == "0") exit(1);
		int number {stoi(lineNumber)};

		while (number != 1 && number != 4)
		{
			number = 0;

			for (char digit : lineNumber)
			{
				number += squared((int)digit-'0');
			}
			lineNumber = to_string(number);
		}

		if (number == 1) cout<<1<<endl;
		else cout<<0<<endl;
	}
}
