#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        long long int n,sum=0,sum1=0;
        cin>>n;
        vector<int> v(n);
        int count=INT_MAX;
        for (int i = 0; i < n; i++)
        {
           cin>>v[i];
           sum+=v[i];
        }
        sum1=sum;
        if(sum%2==0) cout<<"0"<<endl;
        else 
        {
            sort(v.begin(),v.end());
           for (int i = 0; i < n; i++)
        {
            int p=0;
            sum=sum1;
            while(v[i]!=0 && (sum%2)!=0)
            {
                sum-=v[i];
                v[i]=v[i]/2;
                sum+=v[i];
                p+=1;
            }
           if((sum%2)==0) 
           {
            
            count=min(p,count);
           }

        } 
        cout<<count<<endl;
        }
       
   
    }
    return 0;
}