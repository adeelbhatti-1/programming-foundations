#include<iostream>
using namespace std;
main()
{
	int x;
	cin>>x;
	if(x%4==0&&x%6==0)
	{
		cout<<"The number is divided by both";
	}
	else
	{
		if(x%4==0)
		{cout<<"the number is divided by 4";
		}
		if(x%6==0)
		{
			cout<<"THe number is divided by 6";
		}
		else
		{cout<<"The number is not divided by both";
		}
	}
}
