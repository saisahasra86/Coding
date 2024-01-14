#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int a,b,c;
        cin>>a>>b>>c;
        vector<int>v;
        v.push_back(a);
        v.push_back(b);
        v.push_back(c);
        // v.erase(max(max(a,b),c));
        // v.erase(min(min(a,b),c));
        //  cout<<v[0]<<endl;
        sort(v.begin(),v.end());
        cout<<v[1]<<endl;
      
    }
    return 0;
}