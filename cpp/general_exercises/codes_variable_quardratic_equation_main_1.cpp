# include <iostream>
using namespace std;
int main(){
    int number;
    int digit;
    cout<<"Please enter a 4 digit integer"<<endl;
    cin>>number;
    digit = number%10;
    cout<<"digit is : "<<digit<<endl;
    number = number/10;
    digit = number%10;
    cout<<"digit is : "<<digit<<endl;
    number = number/10;
    digit = number%10;
    cout<<"digit is : "<<digit<<endl;
    number = number/10;
    digit = number%10;
    cout<<"digit is : "<<digit<<endl;
    number = number/10;
    digit = number%10;
    

    



  
return 0;



}