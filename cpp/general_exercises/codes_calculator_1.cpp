#include<iostream>
using namespace std;
int main()
{
	char opr;
	float x,y;
	float res;
	cout<<"Please input the operator : "; cin>>opr;
	cout<<"Please input first and second number :"; cin>>x>>y;
	switch(opr)
	{
		case '+':
		res=x+y; cout<<"Here is your result "<<res;
		break;
		case '-':
		res=x-y; cout<<"Here is your result "<<res;
		break;
		case '*':
		res=x*y; cout<<"Here is your result "<<res;
		break;
		case '/':
		res=x/y; cout<<"Here is your result "<<res;
		break;
		default:
			cout<<"Invalid Operator";
	}
}
