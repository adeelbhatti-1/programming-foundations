#include<iostream>
#include<graphics.h>
#include<conio.h>
using namespace std;
int main()
{
	int gd=DETECT,gm;
	initgraph(&gd,&gm,"C:\\tc\\bgi");
	circle(300,300,30);
	closegraph();
	getch();
}