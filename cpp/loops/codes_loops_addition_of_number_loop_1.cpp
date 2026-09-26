# include <iostream>
using namespace std;
int main(){
  /* int sum;
   int count{100};
   int z;
    for (size_t i = 0; i < count; i++)
    {
        z = ++i;
     sum = i+z;
     cout<<sum;
    }
    
   double sum {2}; 
   double  number = 1;
   double count;
   cout<<"Please input your wishable sum"<<endl;
   cin>>count;
  // int c = 1234567891;
   while (number<=count)
   {
      sum = number + number;
      number = ++number;

   }
   cout<<"Sum of the first 1000 : "<<sum<<endl;
//cout<<c;*/
int esum =0;
int osum = 0;
int number =1;
int count;
cout<<"Please input your wishable sum"<<endl;
 cin>>count;
while (number<=count)
{
   if (number%2 ==0)
   {
      esum +=number;
   }else{
      osum +=number;
   }
   ++number;
} cout<<"Even number Sum : "<<esum<<endl;
cout<<"Odd number Sum : "<<osum<<endl;
cout<<"Total Sum : "<<esum+osum<<endl;

}