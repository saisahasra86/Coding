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
        vector<int> v(n);
        for(int i=0;i<n;i++)
        {
            cin>>v[i];
        }
        sort(v.begin()+1,v.end());
        for(int i=1;i<n;i++)
        { 
            if(v[0]<v[i]){
  v[0]=ceil((v[i]+v[0])/2.0);
            }
          
        }
        cout<<v[0]<<endl;
    }
    return 0;
}