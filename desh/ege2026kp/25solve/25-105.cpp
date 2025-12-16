// Автор: М. Нехорошева

#include<iostream>
#include<cmath>
using namespace std;// 523456; 578925

int isPrime( int x )
 {
 	if (x <= 1) 
  		return 0;
  	for (int d = 2;d<=x/2;++d)
    	if (x % d == 0)
      		return 0;    
  	return 1;
  } 
int main()
{
	int m[1000],k=0;
	for (int i=101;i<998;i+=2)
		if (isPrime(i))
			{
				m[k]=i;
				++k;
				//cout<<i<<" \t";
			}
	cout<<"\n";
	int c1=100000000,c2=10;
	for (int i=0;i<k-1;++i)
		for (int j=i+1;j<k;++j)
			if (m[i]*m[j]>523456 && m[i]*m[j]<578926 && abs(m[i]-m[j])< abs(c1-c2) )
				{
					c1=m[i];
					c2=m[j];
				}
	cout<<c1<<"\t"<<c2<<"\t"<<c1*c2;
}

