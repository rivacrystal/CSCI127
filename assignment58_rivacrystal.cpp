//Name: Riva Crystal
//Email: riva.crystal@gmail.com
//Date: November 27, 2021
//This program makes a trapezoid

#include <iostream>
#include <string>
using namespace std;

int main() {
	int num;
	char sym;
	int x = 0;

	cout << "Please enter a number: ";
	cin >> num;
	cout << "Please enter a character: ";
	cin >> sym;

	while (x <= num) {
		cout << string(x, sym) << "\n";
		x++;
	}

	for (int i = 0; i < num; i++) {
		cout << string(num, sym) << "\n";
	}
}