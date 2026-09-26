# include <iostream>

using namespace std;
int main(){
    float a,b,y,z,x,mark,percentage;
cout<<"Please enter Computer subject marks\n";
cin>>x;
cout<<"Please enter Biology subject marks\n";
cin>>z;
cout<<"Please enter Physics subject marks\n";
cin>>b;
cout<<"Please enter Math subject marks\n";
cin>>a;
cout<<"Please enter Chemistry subject marks\n";
cin>>y;
mark = (x+y+z+a+b);
percentage = (mark/500)*100;
if (percentage >=90 )
{
    cout<<"Your Grade is A \n";
}
if (percentage >=80 && percentage < 90)
{
    cout<<"Your Grade is B \n";
}
if (percentage >=70 && percentage < 80)
{
    cout<<"Your Grade is C \n";
}if (percentage >=60 && percentage < 70)
{
    cout<<"Your Grade is D \n";
}
if (percentage >=40 && percentage < 60)
{
    cout<<"Your Grade is E \n";
}if (percentage < 40)
{
    cout<<"Your Grade is F \n";
}

cout<<"Total Percentage : "<<percentage<<"%"<<endl;



return 0;
}