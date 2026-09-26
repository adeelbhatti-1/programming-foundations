#include<iostream>
using namespace std;
int main()
{
	int a[2][2];
	for(int i=0;i<2;i++)
	{
		for(int j=0;j<2;j++)
		{
			cout<<"Please input the value of "<<i<<"th row and "<<j<<"th coloumn :"; cin>>a[i][j];
		}
	}
	cout<<"The matrix is : "; cout<<endl;
	for(int i=0;i<2;i++)
	{
		for(int j=0;j<2;j++)
		{
			cout<<a[i][j]<<"    ";
		}
	cout<<endl;
	}
	cout<<endl;
	cout<<a[0][0]<<"  "<<a[0][1]<<"   "<<a[1][0]<<"   "<<a[1][1];
}