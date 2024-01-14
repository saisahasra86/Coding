#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int x=0;
        int y=0;
        int n;
        cin>>n;
        string s;
        int flag=0;
        for(int i=0;i<n;i++) cin>>s[i];
        for(int i=0;i<n;i++)
        {
            if(s[i]=='U') y+=1;
            else if(s[i]=='L') x-=1;
            else if(s[i]=='D') y-=1;
            else x+=1;
            if(x==1 && y==1) 
            {
                flag=1;
                cout<<"Yes"<<endl;
                break;
            }
        }
    if(flag==0) cout<<"No"<<endl;  
    }
    return 0;
}