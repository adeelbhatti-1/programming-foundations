#include<iostream>
using namespace std;
int main()
{
	string s1,s2;
	cout<<"Input S1 :"; cin>>s1;
	cout<<"Input S2 :"; cin>>s2;
	//s1=s1+s2;//or we can use "append" instead s1=s1+s2
	s1.append(s2);
	cout<<"Output of S1"<<s1;
	
}
