#include<iostream>
using namespace std;
int main()
{
int z;
int i;
	int a[100];
	for(i=0;i<100;i++)
	{
		a [i]=i ;
	}
	cout <<"Please enter a positive integer";
	cin >>z;
	int found=0;
	if(found==1)
	cout<<"We found the integer at position"<<i;
	else 
		cout <<"The number was not found";
}
