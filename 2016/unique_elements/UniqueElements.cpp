#include <iostream>
#include <fstream>
#include <unordered_set>
#include <string>

using namespace std;

int main (int argc, char **argv)
{
	ifstream input {argv[1]};
	for (string line; getline(input, line);)
	{
		unordered_set<string> us {};
		string num {""};
		string outputline {""};
		for (char c : line)
		{
			if (c == ',')
			{
				if (us.insert(num).second)
				{
					outputline.append(num+',');
				}
				num = "";
			}
			else
			{
				num.push_back(c);
			}
		}
		if (us.insert(num).second)
		{
			outputline.append(num);
		}
		else
		{
			outputline.pop_back();
		}
		cout<<outputline<<endl;
	}
}
