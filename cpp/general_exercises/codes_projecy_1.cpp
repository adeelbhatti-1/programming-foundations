#include<iostream>
using namespace std;
int main()
{
	int x=98;
	int y;
	cout<<"Let's play a game , can you guess the number that I have input";
	cout<<endl;	cout<<"Now start your guess"; cout<<endl;
	cout<<"Remember You have 5 tries , if you guessed it correctly"; cout<<endl; cout<<" you will get a tea from me";
	cout<<endl;	cout<<"Please input your guess";
	cin>>y;
	if(x-y>0)
	{cout<<"You should consider a larger number";	cout<<endl;}
	if(x-y<0)
	{cout<<"You should consider a smaller number"; cout<<endl;}
	if(x-y<10&&x-y>0)
	{cout<<"You are quite close"; cout<<endl;}
	if(x-y>-10&&x-y<0)
	{cout<<"You are quite close"; cout<<endl;}
}
