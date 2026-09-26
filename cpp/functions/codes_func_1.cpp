#include<iostream>
using namespace std;
void val(int *x)
{
	*x=5;
	return;
}
int main()
{
	int a=2;
	cout<<"Here is value of a before function : "<<a;
	val(&a);
	cout<<"Here is value of a after function : "<<a;
}