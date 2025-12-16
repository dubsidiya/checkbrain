// Автор: М. Нехорошева

#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
int main()
{
	long long int n,i;
	cin>>n;
	long long int ch[n];
	for (long long int i=0;i<n;++i)
		ch[i]=i+1;
	for (long long int i=1;i<sqrt(n);++i)
			for (long long int j=i+1;j<n;++j)	
				if (ch[j]%i==0 )
					ch[j]=0;
	long long int n1=0;
	for (long long int i=0;i<n;++i)	
		if (ch[i]!=0) 
		{
			++n1;
		//	cout<<ch[i]<<"  ";
		}
//	system ("pause");
	long long int b[n1];
	long long int n2=0,i1,i2,d1,d2,d3;
	for (long long int i=0;i<n;++i)
		if (ch[i]!=0)
		{
			++n2;
			b[n2]=ch[i];
		}
	int k=0;
	for (long long int i=1;i<n2-1;++i)
		for (long long int j=i+1;j<n2;++j)
			if (b[i]*b[j]>264871 && b[i]*b[j]<=322989 && b[i]%10==b[j]%10)
				++k;
	cout <<k;

}
