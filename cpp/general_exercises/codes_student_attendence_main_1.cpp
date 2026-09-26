# include <iostream>

using namespace std;
int main(){
float x;
float totalpercentage;
cout<<"Please enter attadence of CLass Calculus\n";
cin>>x;
totalpercentage = (x/30)*100;
if(totalpercentage>=70){
    cout<<"Allow in Exam-Hall";
}else{
     cout<<"Not Allow in Exam-Hall";
}
return 0;
}