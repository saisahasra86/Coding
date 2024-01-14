#include<bits/stdc++.h>
using namespace std;
int main()
{
   int n,a,b;
   cin>>n>>a>>b;
   if(n>(a+b))
   {
      int k=n-a-b;
    cout<<(n-(a+b))<<endl;
    while(a--)
    {
        cout<<"1"<<":"<<"0"<<endl;
    }
    while(b--)
    {
      cout<<"0"<<":"<<"1"<<endl;  
    }

  
    while((k)--)
    {
        cout<<"0"<<":"<<"0"<<endl;
    }
    
   }
   else
   {
    cout<<"0"<<endl;
    if(a=0) cout<<"0"<<":"<<""<<endl;
   }
    return 0;
}