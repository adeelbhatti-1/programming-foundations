#include<iostream>
#include<string>
using namespace std;
int main()
{
	int x;
	string s1="university";
	string s2="university";
	x=s1.compare(s2);
	cout<<"The value in x : "<<x<<endl;
	if(x==0)
	cout<<"arrays are equal";
	else 
	cout<<"arrays are not equal"; 
}
