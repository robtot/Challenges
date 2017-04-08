#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int main(int argc, char** argv) {
  ifstream infile(argv[1]);
  string line;
  while (getline(infile, line)) {
    cout << line << endl;
  }

}
