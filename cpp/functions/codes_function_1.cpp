#include<iostream>
using namespace std;
double fac(int n)
{
	if(n==1)
	return 1;
	else
	return n*fac(n-1);
}
int main()
{
	int n;
	cout<<"Please input the number , you want the factorial of : "; cin>>n;
	cout<<"Here is your factrial : "<<fac(n);
}