#include<iostream>
using namespace std;
int main()
{
	int x,y,z=2,a;
	cout<<"THE COMPOSITE NUMBER CALCULATOR"<<endl<<"_______________________________"<<endl;
	cout<<"Please input the lower input : "; cin>>x; cout<<endl;
	cout<<"Please input the upper input : "; cin>>y; cout<<endl;
	do
	{
		if(x%z==0&&x!=z)
		{
		}
		else
		{
			cout<<x<<"  ";	
			if(x=z)
			x++;
		}
	}while(z<x);
}
