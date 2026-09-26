#include<iostream>
using namespace std;
int main()
{
	int x;
	cout<<"Please input the number : "; cin>>x;
	switch(x>0)
	{
		case 1:
			cout<<"Your number is positive";
			break;
		case 0:
				switch(x<0)
				{
					case 1:
					cout<<"Your number is negative";
					break;
					case 0:
					cout<<"Your number is zero";
				}
	}
}
