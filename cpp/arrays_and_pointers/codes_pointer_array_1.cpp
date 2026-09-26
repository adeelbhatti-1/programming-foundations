#include<iostream>
using namespace std;
int main()
{
	int a[]={53,22,33,55};
	int *p;
	p=a;
	cout<<"This is p : "<<p<<'\t'; cout<<*p<<endl; p=p+1;
	cout<<"This is p : "<<p<<'\t';	cout<<*p<<endl;	p=p+1;
	cout<<"This is p : "<<p<<'\t';	cout<<*p<<endl;	p=p+1;
	cout<<"This is p : "<<p<<'\t';	cout<<*p<<endl;	p=p+1;
	/*	for(int i=0;i<4;i++)
		{
			cout<<*p<<'\t';
			p=p+1;
		}
	*/
}