#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main (int argc, char **argv)
{
	ifstream inputFile {argv[1]};
	string inputLine {};

	while (getline(inputFile, inputLine))
	{
		int dividerX {};
		int dividerY {};
		int count {};
		bool isFirstSpace {true};
		string numberBuffer {};

		for (char character : inputLine)
		{
			if (character==' ' && isFirstSpace) {
				dividerX = stoi(numberBuffer);
				numberBuffer = "";
				isFirstSpace=false;
			}
			else if (character==' ' && !isFirstSpace) {
				dividerY = stoi(numberBuffer);
				numberBuffer = "";
			}
			else
				numberBuffer.push_back(character);
		}
		count = stoi(numberBuffer);
		numberBuffer = "";

		for (int i = 1; i <= count; i++)
		{
			bool isDivisible {false};
			if (i%dividerX==0) {
				numberBuffer.push_back('F');
				isDivisible = true;
			}
			if (i%dividerY==0) {
				numberBuffer.push_back('B');
				isDivisible = true;
			}
			if (!isDivisible)
				numberBuffer.append(to_string(i));
			numberBuffer.push_back(' ');
		}
		numberBuffer.pop_back();
		cout<<numberBuffer<<endl;
	}
}
				
