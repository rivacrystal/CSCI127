//Name: Riva Crystal
//Email: riva.crystal@gmail.com
//Date: November 26, 2021
//This program does a little countdown

#include <iostream>
#include <string>
using namespace std;

int main()
{
	int number;
	string word;

	cout << "Please enter a number: ";
	cin >> number;

	cout << "Please type a word: ";
	cin >> word;

	cout << word;

	while (number > 0) {
		cout << number << ",\n";
		number--;
	}

	cout << "Time for " << word << "!\n";
	return 0;
}