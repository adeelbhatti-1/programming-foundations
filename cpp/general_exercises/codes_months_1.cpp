#include<iostream>
using namespace std;
int main()
{
	int i;
	cout<<"Please input the number of month :"; cin>>i;
	switch(i)
	{
	case 1:
	cout<<"Jan with 31 days";
	break;
	case 2:
	cout<<"Feb with 28 days";
	break;
	case 3:
	cout<<"March with 31 days";
	break;
	case 4:
	cout<<"April with 30 days";
	break;
	case 5:
	cout<<"May with 31 days ";
	break;
	case 6:
	cout<<"June with 30 days ";
	break;
	case 7:
	cout<<"July with 31 days ";
	break;
	case 8:
	cout<<"August with 31 days";
	break;
	case 9:
	cout<<"September with 30 days";
	break;
	case 10:
	cout<<"Oct with 31 days";
	break;
	case 11:
	cout<<"Nov with 30 days";
	break;
	case 12:
	cout<<"Dec with 31 days";
	break;
	default:
	cout<<"Out of domain of months";
	}	
}
