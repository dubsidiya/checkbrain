// Автор: М. Нехорошева

//Найдите максимальную длину цепочки вида DBACDBACDBAC.... (состоящей из фрагментов DBAC, последний фрагмент может быть неполным).
#include <iostream>
#include <fstream>
using namespace std;

int main() 
{
	fstream F;  //открываем файл в режиме чтения  
	F.open("k7b-2.txt");
	char c;
	int k_max=0,k=0;
	for (;!F.eof();)
	{
		F>>c;
		if ((c=='D'&& k%4==0) || (c=='B'&& k%4==1)	|| (c=='A'&& k%4==2) || (c=='C'&& k%4==3))
								{
									++k;
									if (k> k_max )
											k_max=k;}
									else 
										if (c=='D') k=1;	
											else k=0;														
	}
	cout<<k_max;


}
