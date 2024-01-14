#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        string s;
        cin>>s;
        string subs1,subs2;
        for(int i=0;i<s.size();i++)
        {
                  if(s[i]=='+') 
                  {
                    subs1=s.substr(0 , i);
                    subs2=s.substr(i+1,((s.size())-i-1));
                    break;
                  }
        }
    cout<<(stoi(subs1)+stoi(subs2))<<endl;
    }
    return 0;
}