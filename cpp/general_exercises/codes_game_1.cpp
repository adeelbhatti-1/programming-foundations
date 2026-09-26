#include<iostream>
#include<stdlib.h>
using namespace std;
int main()
{
	int onum,guess,tries;	//onum=original number guess=user's guessed number	tries=number of tries by user
	cout<<"Game is simple , You input a number other person will guess "; cout<<endl;	
	cout<<"Don't worry, player will get the required hints "; cout<<endl;
	cout<<"to make the game interesting keep your number between 1 and 1000"; cout<<endl;	
	cout<<"Please input your number: ";
	cin>>onum;
	system("cls");
	do
	{
		cout<<"Please input your guess: ";	cin>>guess;
		if(0<onum-guess&&onum-guess<=5)
		{cout<<"You are extremely closer"; cout<<endl;}
		if(0>onum-guess&&onum-guess>=5)
		{cout<<"You are extremely closer"; cout<<endl;}
		else
		{
			if(0<onum-guess&&onum-guess<=30)
			{cout<<"You are closer"; cout<<endl;}
			if(0>onum-guess&&onum-guess>=30)
			{cout<<"You are closer"; cout<<endl;}
			else
			{
				if(0<onum-guess&&onum-guess<=100)
				{cout<<"You are too far away better get some sleep"; cout<<endl;}
				if(0>onum-guess&&onum-guess>=100)
				{cout<<"You are too far away better get some sleep"; cout<<endl;}
			}
		}
		if(guess==onum)
		{cout<<"Congratulations! You have guessed the right number"; tries=8;}
		else
		{
		tries=tries+1;
		}
		if(tries==7)
		cout<<"You have attempted for the maximum times , try again next time";
	}while(tries<=6);
	
}
