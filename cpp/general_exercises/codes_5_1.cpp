#include<iostream>
using namespace std;
int main()
{
	int x,y;
	cout<<"Please input the number you want to check wether it is odd or even : ";
	cin>>x;
	switch(x>=0)
	{
	case 1:
		cout<<"Your number is positive";
		break;
	case 0:
		cout<<"Your number is negative";
	}
}
