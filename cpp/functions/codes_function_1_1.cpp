#include<iostream>
using namespace std;
void display(int n)
{
	if(n<1)
	return;
	else
	cout<<n<<endl;
	cout<<"Calling";
	display(n-1);
	cout<<"called ";
	cout<<n<<endl;
}
main()
{
	int n=3;
	display(n);
	return 0;
}
