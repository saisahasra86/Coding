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
        vector<int>v;
        string p = "abcdefghijklmnopqrstuvwxyz";
        for(int i=0;i<n;i++) 
        {
            for(int j=0;j<26;j++)
            {
                if(s[i]==s[j]) v.push_back(j+1);
            }
        }
        sort(v.begin(),v.end());
        cout<<v.back()<<endl;
    }
    return 0;
}