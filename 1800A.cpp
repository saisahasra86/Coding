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
        unordered_set<char>st;
        vector<char>v;
        for (int x=0; x<n; x++)   s[x]=toupper(s[x]);
        for (int j=0; j<n; j++)  
        {
            if(st.find(s[j])==st.end()) 
            {
                st.insert(s[j]);
                v.push_back(s[j]);
            }  
        }
        string t="MEOW";
        int p=0;
        if(v.size()==4)
        {
            for(auto ch : v)
        {
            if(p<4 && ch==t[p]) 
            {
                p++;
                if(p==3) 
                {
                    cout<<"Yes"<<endl;
                    break;
                } 
            }  
            else 
            { 
                cout<<"No"<<endl;
                break;
            }
        }

        }
        else cout<<"No"<<endl;
        
        
      
    }
    return 0;
}