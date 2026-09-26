#include<iostream>
using namespace std;
int main()
{
	int x,y;
	cout<<"Please input two numbers one after the other :"; cin>>x>>y;
	switch(x>y)
	{
		case 1:
		cout<<x<<" is maximum"<<endl<<y; break;
		case 0:
		cout<<x<<endl<<y<<" is maximum"; break;
		default:
		cout<<"Both are equal";
	}
}
