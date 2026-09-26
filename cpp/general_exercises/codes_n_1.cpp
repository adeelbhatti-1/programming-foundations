#include<iostream>
using namespace std;
int main()
{
	int number;
	int factorial=1;
	cout<<"Welcome to the World of Mathematics"<<endl;
	cout<<"Please input a number  : ";
	cin>>number;
	while(number>1)
	{
		factorial=factorial*number;
		number=number-1;
	}
	cout<<factorial;
}
