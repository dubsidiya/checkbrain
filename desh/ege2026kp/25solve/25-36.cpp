// Автор: М. Нехорошева

#include <iostream>
#include <cmath>
using namespace std;
long int s;

int main()
{setlocale(LC_ALL,"Rus");
   for (int i=194441;i <= 196500;i++)
    {
      int k=0,max=0;
      for(int j=2;j<=i/2;++j) 
      	if (i%j==0)
		  {
      		++k;
			if (j*j==i)
				max=j;  	
		  }
	  if (k%2==1 and max!=0)
	  	cout << 1<< "\t" <<max<<"\t"<<i<<"\t"<<"Ра Си Я, я люблю есть колбасу и танцевать"<<endl;
	  	
    }
  
}

