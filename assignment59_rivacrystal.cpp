//Name: Riva Crystal
//Email: riva.crystal@gmail.com
//Date: November 29, 2021
//This program works on a budget

#include <iostream>
#include <iomanip>
using namespace std;

int main () {
	float budget;
	float coffee;

	cout << "Enter your monthly budget for food and coffee: ";
	cin >> budget;
	cout << "How much are you spending in a week for coffee: ";
	cin >> coffee;

	for (int i = 1; i < 5; i++)
	{
		budget = budget - coffee;
		cout << fixed << setprecision(2) << "Budget left after week " << i << "\t" << budget << "\n";
	}
}