#include<iostream>
using namespace std;
int main()
{
	char c;
	int x=1,y=5;
	cout<<"Please input your guess ";
	cin>>c;
	while((x<=5)&&(c!=5))
	{
		cout<<"Please input your guess ";
	cin>>c;
	x=x+1;
	}
}
