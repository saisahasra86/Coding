#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        string s;
        cin>>s;
        int flag=0;
         for(int i=1;i<n;i+2)
        {
        if((%2)==0) 
         {
            if(s[i]==s[i+1]) 
            {
                i=i+1;
                flag=1;
            }
            else 
            {
                flag=0;
            }

         }
        }
        if(flag==1) cout<<"yes"<<endl;
        else cout<<"no"<<endl;
    }
return 0;
}
    
