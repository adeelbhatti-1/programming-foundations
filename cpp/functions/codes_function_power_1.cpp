#include<iostream>
int x;
using namespace std;
float sq()
{
	int n;
	if(n==0)
	return 1;
	else
	{
	return x*sq(n-1);
	cout<<"First execution ,";
	}
}
int main()
{
	int n;
	cout<<"Please input the value of base : "; cin>>x;
	cout<<"Please input the value of exponenet : "; cin>>n;
	sq(n);
	cout<<"Your result : "; cout<<sq(n);
}