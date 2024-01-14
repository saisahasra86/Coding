#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
       int n,k;
       cin>>n>>k;
       string s;
       for(int i=0;i<n;i++) cin>>s[i];
       for(int i=0;i<n;i++)
       {
        for(int j=0;j<n;j++)
        {
          if((s[i]==(s[j].lower())) || (s[i]==(s[j].upper()))) 
          {
            s.erase(s[i]);
            s.erase(s[j]);
          }
        }
       } 
         
    }
    return 0;
}