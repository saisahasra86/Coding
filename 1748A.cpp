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
    int count=0;
    if(s[0]=='1') count=1;
    for(int i=1;i<n;i++)
    { 
        if(s[i]=='1')
        {
            count++;
              if(count%2==0) cout<<'-';
        else cout<<'+';
        }
        else cout<<'+';
      
    }
    cout<<endl;
    }
    return 0;
}