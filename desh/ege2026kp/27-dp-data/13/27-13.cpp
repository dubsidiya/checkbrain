// Автор: М. Нехорошева

#include <iostream>
#include <fstream>
using namespace std;
int main ()
{
	ifstream f;
	f.open("27-13b.txt");
	int k=0,n;
	f>>n;
	int a[n];
	for(int i=0;i<n;++i)
		f>>a[i];
	int r=max(a{});
	for(int i=0;i<n-7;++i)	
		for(int j=i+7;j<n;++j)
			if((a[i]*a[j])%14==0 )
				++k;
	cout<<k;
}
