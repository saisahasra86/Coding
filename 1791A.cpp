#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        string s;
        s = "codeforces";
        char r;
        cin>>r;
        int flag=0;
        for(int i=0;i<s.size();i++)
        {
            if(r==s[i]) 
            {
                flag=1;
                break;
            }
        }
        if(flag==1) cout<<"Yes"<<endl;
        else cout<<"No"<<endl;
    }
    return 0;
}