/*# include <iostream>

using namespace std;
int main(){
 char str;
char count;
cout<<"Please any word"<<endl;
cin>>str;
count = str;
cout<<++count;


return 0;}
# include <conio.h>
#include <iostream>
//# include <conio.h>
#include <stdio.h>
using namespace std;
 
int main()
{
    char str[100];
    int i,totChar;
totChar=0;
    cout<<"Please enter the string for count characters\n";
    gets(str);//gets and store string from useer
//count characters of a string wit out space
    for(i=0; str[i] != '\0'; i++){
        if(str[i]!=' ')// this condition is used to avoid counting space
        {
            totChar++;
        }
    }
    cout<<"The total characters of the given string= "<<totChar;
    getch();
    return 0;}*/
 #include <iostream>
#include <string>
using namespace std;
int main()
{

int count = 0;
string s("Hello");
char ignore;

for (int i = 0; i < s.size(); i++) 
    {
       if (s.at(i) == '_')    
           count++;
        
           cout<<count;
    }
return 0;
}

 

