# include <iostream>

using namespace std;
int main(){
int x;
int y;
int max;
int z;
/*cout<<"Please input first number"<<endl;
cin>>x;
cout<<"Please input second number"<<endl;
cin>>y;
cout<<"Please input third number"<<endl;
cin>>z;
if(x>y && x>z)
{cout<<"First number is max: "<<x<<endl;}
if(y>x && y>z){
cout<<"Second number is max: "<<y<<endl;}
if (z>x && z>y)
{cout<<"Third number is max: "<<z<<endl;}
cout<<"#---------------------------#\n";
cout<<"First number is : "<<x<<endl;
cout<<"Second number is : "<<y<<endl; 
cout<<"Third number is : "<<z<<endl;
cout<<"#---------------------------#\n";*/
cout<<"Please input first number"<<endl;
cin>>x;
cout<<"Please input second number"<<endl;
cin>>y;
if(x>y){
    if(x>z){
        max = x;

    }else max = z;
}

return 0;
}