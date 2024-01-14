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
        int count1=0;
        int count2=0;
        int count3=0;
        int count=0;
        vector<int> v;
        for(int i=0;i<4;i++) cin>>v[i];
               x+=v[1];
               y+=v[1];
        for(int i=0;i<v[2];i++)
           {
              y-=1;
              x+=1;
              count1+=1;
            if(y==0) break;
           }
        for(int i=0;i<v[3];i++)
           {
            x-=1;
            y+=1;
            count2+=1;
              if(x==0) break;
           }
        while(count1 !=v[2] && y>0)
        {
            y-=1;
            x+=1;
           count1+=1;
           if(y==0) break;
        }
        while(count2 !=v[3] && x>0)
        {
            x-=1;
            y+=1;
           count2+=1;
           if(x==0) break;
        }
        for(int i=0;i<v[4];i++)
           {
            x-=1;
             y-=1;
            if(x==0 && y==0) break;
            count3+=1;
           }
        count=count+v[1]+count2+count3+count1;
        cout<<count<<endl;


    }
    return 0;
}