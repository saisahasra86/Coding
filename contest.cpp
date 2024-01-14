#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
         int count=0,count1=0,count2=0;
         int n;
         cin>>n;
        int d =n;
        int p=n;
        long long int s= 3141592653589793238462643383279;
        string s1 = to_string(s); 
         while(p!=0)
         {
            int f= p%10;
            p=p/10;
            count+=1;
         }
         while(d!=0)
         {
             count1+=1;
            if(d==stoi(s1.substr(0,count))) 
            {
                while(d!=0)
                {
                    d=d/10;
                    count2+=1;
                }
            } 
             d=d/10;
        }
    cout<<count2<<endl;
    }
   
    return 0;
}