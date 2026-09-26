# include <iostream>

using namespace std;
int main(){
    int intermark;
    int testmarks;
    cout<<"Please input your intermark\n";
    cin>>intermark;
    cout<<"Please input your Testmarks\n";
    cin>>testmarks;
    if ((intermark>=75)&&(testmarks>=50))
    {
        cout<<"You are admitted Sukkur IBA University\n";
    }
    else {
        cout<<"You are luck!(not here in IBA Sukkur) \n";
    }
   /* int amir,amara;
    cout<<"Please enter age of amir"<<endl;
    cin>>amir;
    cout<<"Please enter age of amara"<<endl;
    cin>>amara;

    if (amir>amara)
    {
        cout<<"Amir is older then amara"<<endl;

    }
    else {
        cout<<"amir is less then amara"<<endl;
    }
    if (amir<amara)

    {
        cout<<"amara is older then amir"<<endl;
    }
    if (amir==amara)
    {
        cout<<"amara and amir is equal age"<<endl;
    }*/
    
return 0;
}