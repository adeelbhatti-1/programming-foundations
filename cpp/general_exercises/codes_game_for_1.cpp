#include<iostream>
#include<stdlib.h>
using namespace std;
int main()
{
	int onum,guess,tries;
	cout<<"Please input the number : ";	cin>>onum;
	system("cls");
	for(tries=0;tries>=5;tries++)
	{
		cout<<"Please input your guess";	cin>>guess;
		if(0<onum-guess&&onum-guess<=5)
		{cout<<"You are extremely closer"; cout<<endl;}
		if(0>onum-guess&&onum-guess>=-5)
		{cout<<"You are extremely closer"; cout<<endl;}
		else
		{	if(0<onum-guess<=20||0>onum-guess>=20)
			{cout<<"You are closer try a little better";}
			else
				{cout<<"You are way too far away";}
		}
		if(onum==guess)
		{cout<<"Congratulations! You have guessed the right number";	tries=6;}
	}
	cout<<endl;
	cout<<"You have attempted for the maximum times better try next time";
}
