#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	string read;
	char name[100],school[50],cls[20],cms[20];
	fstream file;
	/*file.open("file handling 3.txt",ios::app);
	cout<<"Enter your name : ";
	cin.getline(name,100);
	cout<<"Enter your School : ";
	cin.getline(school,50);
	cout<<"Enter your class : ";
ss	cin.getline(cls,20);
	cout<<"Enter your CMS ID : ";
	cin.getline(cms,20);
	file<<endl<<name<<endl<<school<<endl<<cls<<endl<<cms<<endl;
	file.close();*/
	file.open("File handling 3.txt",ios::in);
	while(getline(file,read))
	{
		cout<<read<<endl;
	}
	file.close();
}