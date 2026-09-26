# include <iostream>

using namespace std;
int main(){
int age1,age2,age3,age4,age5,age6,age7,age8,age9,age10;
int TotalAge;
int AverageAge;
cout<<"please enter age of student1"<<endl;
cin >>age1;
cout<<"please enter age of student2"<<endl;
cin>>age2;
cout<<"please enter age of student3"<<endl;
cin >>age3;
cout<<"please enter age of student4"<<endl;
cin>>age4;
cout<<"please enter age of student5"<<endl;
cin>>age5;
cout<<"please enter age of student6"<<endl;
cin>>age6;
cout<<"please enter age of student7"<<endl;
cin>>age7;
cout<<"please enter age of student8"<<endl;
cin>>age8;
cout<<"please enter age of student9"<<endl;
cin>>age9;
cout<<"please enter age of student10"<<endl;
cin>>age10;
TotalAge = age1+age2+age3+age4+age5+age6+age7+age8+age9+age10;
cout <<"Total age of class :  "<<TotalAge<<endl;
AverageAge = TotalAge/10;
cout <<"The average age of class is : "<<AverageAge<<endl;

return 0;

}