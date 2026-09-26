# include <iostream>
using namespace std;
int main(){

int factorial = 1;
int number =1;
int count;
cout<<"Please input your wishable factorial"<<endl;
 cin>>count;
while (number<=count)
{
 
      factorial = factorial*number;
++number;
}

cout<<"factorial : "<<factorial<<endl;

  return 0;
  }