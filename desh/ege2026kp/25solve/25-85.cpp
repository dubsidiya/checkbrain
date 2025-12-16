// Автор: М. Нехорошева

#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
int main()
{
	int n,i,n2=-1,k=0;
	cin>>n;
	int ch[n],b[n];
	for (int i=0;i<n;++i)
		ch[i]=i+1;
	for (int i=2;i<sqrt(n);++i)
			for (int j=i+1;j<n;++j)	
				if (ch[j]%i==0 )
					ch[j]=0;
	for (int i=0;i<n;++i)
		if (ch[i]!=0)
		{
			++n2;
			b[n2]=ch[i]*ch[i];
		}
	for (int i=0;i<n2;++i)
		if (b[i]>3660 &&  b[i]<33626)
			++k;
	cout <<k;									
}
