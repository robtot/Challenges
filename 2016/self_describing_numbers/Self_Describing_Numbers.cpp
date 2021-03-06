#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int findOccurences(string base, string occurence)
{
	int count {0};
	size_t start {0};
	while ((start = base.find(occurence, start)) != string::npos)
	{
		count++;
		start++;
	}
	return count;
}

int main(int argc, char **argv)
{
	ifstream input {argv[1]};
	string line {};

	while (getline(input,line))
	{
		int indexOccurences {};
		int indexNum {};
		bool selfDescribing {true};
		for (int index{0}; index<line.size(); index++)
		{
			indexNum = line[index]-'0';
			indexOccurences = findOccurences(line, to_string(index));
			if (indexNum!=indexOccurences)
			{
				selfDescribing = false;
				break;
			}
		}
		if (selfDescribing)
			cout<<1<<endl;
		else
			cout<<0<<endl;
	}
	return 0;
}
