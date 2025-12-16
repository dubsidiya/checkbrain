// Автор: М. Нехорошева

#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

int isPrime( int x )
 {
 	if (x <= 1) 
  		return 0;
  	for (int d = 2;d<x/2;++d)
    	if (x % d == 0)
      		return 0;    
  	return 1;
  } 
int main() 
{
	int count = 0,b=5336748, e=5336834;
	for ( int i=b; i<e+1;++i )
  		if (isPrime(i))
    	{
    		count += 1;
    		cout<< count<<"\t"<< i<<"\n";	
    	}
}

