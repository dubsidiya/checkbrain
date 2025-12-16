// Автор: М. Нехорошева

/*В текстовом файле k7-84.txt находится цепочка из символов латинского алфавита
 A, B, C. Найдите длину самой длинной подцепочки, состоящей из символов C.*/
#include <iostream>
#include <fstream>
using namespace std;

int main() 
{
	fstream F;  //открываем файл в режиме чтения  
	F.open("k7-84.txt");
	string s;
	getline(F,s);
	int k=0,k_max=0;
	for (int i=0;i<s.size()-1;++i)
		if (s[i]=='C')
			++k;
		else
		{
			k_max=max(k,k_max);	
			k=0;
		}
	cout<<k_max;		
}

