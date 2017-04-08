#include <iostream>
#include <fstream>


using namespace std;

int main (int argc, char **argv)
{
	ifstream input {argv[1], ios::ate | ios::binary};
	cout<<input.tellg()<<endl;
	return 0;
}
