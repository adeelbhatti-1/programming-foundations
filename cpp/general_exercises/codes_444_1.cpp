#include<iostream>
using namespace std;
int main()
{
	int guess,count,number=3;
	do
	{
		cout<<"Please input your guess : "; cin>>guess;
		if(guess==number)
		{
			cout<<"Congratulations, You have guessed the right number ";
			count=6;
		}
		else
		{
			cout<<"Please try again "; cout<<endl;
			count++;
			if(count==6)
			cout<<"You have attempted for the maximum times";
		}
	}while(count<5);
}
