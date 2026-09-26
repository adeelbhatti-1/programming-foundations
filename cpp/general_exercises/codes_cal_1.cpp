#include<iostream>
using namespace std;
int main()
{
	char ch;
	int x,y;
	cout<<"Please input the operator : "; cin>>ch; cout<<endl;
	cout<<"Please input 1st number : "; cin>>x;	cout<<endl;
	cout<<"Please input 2nd number : "; cin>>y;	cout<<endl;
	switch(ch)
	{
	case '*':
	cout<<"your result of multiplication : "<<x*y;
	break;
	case '-':
	cout<<"Your result of substraction : "<<x-y;
	break;
	case '+':
	cout<<"your result of addition : "<<x+y;
	break;
	case '/':
	cout<<"Here is your result of division"<<x/y;
	break;
	default:
	cout<<"Incorrect operator"; 
}
}