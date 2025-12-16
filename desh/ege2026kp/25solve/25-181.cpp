// Автор: М. Нехорошева

#include<iostream>
#include<cmath>
using namespace std;
int main()
{
	int n=pow(97,3)+1,k=0;
	for(int i=n;k!=5;++i)
	{
		int k1=0,m=10000;
		for (int j=103;j<994;j+=10)
			if (i%j==0)
			{
				++k1;
				m=min(m,j);	
			}
		if (k1==3)
		{
			++k;
			cout<<m<<"\t"<<i<<endl;
		}
	}
}

