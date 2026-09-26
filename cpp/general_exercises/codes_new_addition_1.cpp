#include<iostream>
using namespace std;
int main()
{
	int x[2][3];
	int y[3][2];
	int z[3][3];
	cout<<"Please input the value for 1st 2x3 matrix :"; cout<<endl;
	for(int i=0;i<2;i++)
	{
		for(int j=0;j<3;j++)
		{
			cin>>x[i][j];
		}
	}
	cout<<endl;
	cout<<"Your 1st matrix"; cout<<endl;
	for(int i=0;i<2;i++)
	{
		for(int j=0;j<3;j++)
		{cout<<x[i][j]; cout<<'\t';}
		cout<<endl;
	}
	cout<<endl;
	cout<<"Please input the value for 2nd 2x3 matrix :"; cout<<endl;
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
		{
			cin>>y[i][j];
		}
	}
	cout<<endl; cout<<"Your 2nd matrix :"; cout<<endl;
 for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
		{cout<<y[i][j]; cout<<'\t';}
		cout<<endl;
	}
	cout<<endl;
}
