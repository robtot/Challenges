#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;

int main (int argc, char **argv)
{
	string line;
	ifstream aFile(argv[1]);
	if (aFile.is_open())
	{
		while (getline(aFile, line))
		{
			int n,n2, p1, p2;
			bool nOn, n2On;

			string::size_type pos;
			string::size_type oldPos;
			pos = line.find(',');
			n = atoi(line.substr(0, pos).c_str());
			oldPos = pos;
			pos = line.find(',', pos+1);
			p1 = atoi(line.substr(oldPos+1, pos).c_str());
			oldPos=pos;
			pos = line.find('\n');
			p2 = atoi(line.substr(oldPos+1, pos).c_str());

			n2 = n;
			n = n>>(p1-1);
			n2 = n2>>(p2-1);
			if (n%2==0)
			{
				nOn = false;
			}
			else
			{
				nOn = true;
			}
			if (n2%2==0)
			{
				n2On = false;
			}
			else
			{
				n2On = true;
			}
			if (nOn==n2On)
			{
				cout<<"true"<<endl;
			}
			else
			{
				cout<<"false"<<endl;
			}
		}
		aFile.close();
	}
	else
	{
		cout<<"unable to open argument file!\n";
	}
	return 0;
}
