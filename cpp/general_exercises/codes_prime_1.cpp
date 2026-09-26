#include<iostream>
using namespace std;
int main()
{
	int x,y;
	cout<<"Now we will tell you when you input a number whether it is prime or not"<<endl;
	cout<<"Please input the number : "; cin>>x;
	for(y=2;y<=x;y++)
		if(x%y==0&&x!=y)
		{
			cout<<"Your number is not prime"; cout<<endl;
			cout<<"The smallest number that is dividing it is : "; cout<<y;  y=x;
		}
		else
		{
			if(x!=y)
			{}
			else
			{cout<<"Your number is prime";}
		}
}
