//Name: Riva Crystal
//Email: riva.crystal@gmail.com
//Date: November 26, 2021
//This program converts from crypto

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	float crypto;
	cout << "Enter amount in cryptocurrency: ";
	cin >> crypto;
	cout << fixed << setprecision(2) << crypto << " BTC in USD: $" << crypto * 31901.19 << " USD\n"
	 << crypto << " ETH in USD: $" << crypto * 1901.54 << " USD\n"
	 << crypto << " DOGE in USD $" << crypto * 0.179733 << " USD\n";
	return 0;
}