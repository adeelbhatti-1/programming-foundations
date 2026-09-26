#include<iostream>
using namespace std;
int main()
{
int sum,grade;
int students ;
int average ;
	sum=0;
	students=0;
do
{
	cin>>grade;
	sum+=grade;
	students++;
}while(grade>=0); 
average=sum/students;
cout<<average;
}
