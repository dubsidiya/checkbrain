// Автор: М. Нехорошева

#include <iostream>
#include <fstream>
using namespace std;

int main() 
{
	fstream F;  //открываем файл в режиме чтения  
	F.open("k7c-1.txt");
	int k=0;
	string s;
	getline(F,s);
	for (int i=0;i< s.size()-2;++i)	
			if (s[i]=='B' || s[i]=='C'|| s[i]=='D' )
				if ((s[i+1]=='B' || s[i+1]=='E'|| s[i+1]=='D') && s[i]!=s[i+1])
					if((s[i+2]=='B' || s[i+2]=='E'|| s[i+2]=='C') && s[i+2]!=s[i+1])
						++k;
	cout <<k;	
	
}
