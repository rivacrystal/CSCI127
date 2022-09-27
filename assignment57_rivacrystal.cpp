//Name: Riva Crystal
//Email: riva.crystal@gmail.com
//Date: November 27, 2021
//This determines how the weather feels

#include <iostream>
using namespace std;

int main() {
	int temp;
	cout << "Enter the temperature: ";
	cin >> temp;

	if (temp <= 32) {
		cout << "It's freezing!";
	} else if (temp > 32 && temp < 68) {
		cout << "It's cold!";
	} else if (temp >= 68 && temp < 73) {
		cout << "It's warm!";
	} else {
		cout << "It's hot!";
	}
}