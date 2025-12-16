// Автор: М. Нехорошева

#include <iostream>
using namespace std;
int main()
{
	int k=0;
	for(long int i=10000001;k!=5;++i)
	{
		int s=0,kd=0;
		for (int j=2;j<i/2+1;++j)
			if (i%j==0)
			{
				++kd;
				s+=i/j;
				if (kd==3)
					break;
			}
		if (kd>2)
		{
			int z=s,x=z%10,k1=0,k2=1;
			z/=10;
			for (;z;z/=10)
			{
				if (z%10<=x)
					++k1;
				++k2;
				x=z%10;
			}
			if (k1==k2-1)
				{
					cout<<s<<endl;
					++k;
				}			
		}
	}
}

