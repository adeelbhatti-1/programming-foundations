#include<iostream>
int fun(int n);
using namespace std;
main()
{
	int n;
	cout<<"Please input the number for the factorial "; cin>>n;
	cout<<fun(n);
}
int fun(int n)
{
	if(n==1)
	return n;
	else
	return n*fun(n-1);
}
