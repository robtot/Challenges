#include <iostream>

using namespace std;

int main()
{
	for (int y=1;y<=12;y++)
	{
		for (int x=1;x<=12;x++)
		{
			int xy=x*y;
			if (xy<10)
			{
				cout<<"   "<<xy;
			}
			else if (xy<100)
			{
				cout<<"  "<<xy;
			}
			else
			{
				cout<<" "<<xy;
			}
		}
		cout<<endl;
	}
}
