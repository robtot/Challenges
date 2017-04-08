#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> computePrimes(int upperLimit)
{
	if (upperLimit<2)
		return vector<int>{};

	vector<int> primes {2};

	for (int i = 3; i<=upperLimit; i++)
	{
		bool isPrime {true};
		for (int prime : primes)
		{
			if (i%prime==0) {
				isPrime = false;
				break;
			}
		}
		if (isPrime)
			primes.push_back(i);
	}
	return primes;
}

bool isPalindrome(int integer)
{
	string sInteger {to_string(integer)};
	size_t sIntegerSize {sInteger.size()};
	size_t sIntegerIndex {0};

	if (sIntegerSize == 1)
		return true;
	else if (sIntegerSize == 0)
		return false;
	else {
		sIntegerSize--;
		while (sIntegerIndex < sIntegerSize && sIntegerIndex != sIntegerSize)
		{
			if (sInteger.at(sIntegerIndex) != sInteger.at(sIntegerSize))
				return false;
			sIntegerIndex++;
			sIntegerSize--;
		}
		return true;
	}
}

int main ()
{
	vector<int> primes {computePrimes(1000)};
	for (vector<int>::reverse_iterator rit = primes.rbegin(); rit != primes.rend(); rit++)
	{
		if (isPalindrome(*rit)) {
			cout<<*rit<<endl;
			break;
		}
	}
	return 0;
}
