#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	char ah[40];
	fstream file;
	file.open("happened.txt",ios::app);
	cout<<"Please input the text ";
	cin.getline(ah,40);
	file<<ah<<endl;
	file.close();	
}