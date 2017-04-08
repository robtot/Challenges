#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;

int main (int argc, char **argv)
{
	ifstream input {argv[1]};
	string line;

	while (getline(input, line))
	{
		int sum = 0;
		for (string::iterator it=line.begin(); it!=line.end(); ++it)
		{
			//ints from 0 to 9 begin at 48 so minus 48 from int value gives us the character as int
			sum+=(int)*it-48;
		}
		cout<<sum<<endl;
	}
	return 0;
}
