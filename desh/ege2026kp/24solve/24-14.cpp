// Автор: М. Нехорошева

#include <iostream>
#include <fstream>
using namespace std;

int main() 
{
	fstream F;  //открываем файл в режиме чтения  
	F.open("k7-80.txt");
	int k=0, max=0;
	char c;
	for (;!F.eof();)
	{
		F>>c;
		if (c=='C') ++k;
		else 
		{
			if (k>max)
				max=k;
			k=0;
		}
		
	}
	cout<<max;
}
