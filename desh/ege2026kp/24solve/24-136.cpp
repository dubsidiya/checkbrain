// Автор: М. Нехорошева

//Текстовый файл 24-s1.txt состоит не более чем из 106 заглавных латинских букв (A..Z). 
//Текст разбит на строки различной длины. Определите количество строк, 
//в которых буква J встречается чаще, чем буква E.
#include <iostream>
#include <fstream>
using namespace std;

int main() 
{
	fstream F;  //открываем файл в режиме чтения  
	F.open("24-s1.txt");
	string s;
	int k=0;
	for (;!F.eof();)
	{
		int k_J=0, k_E=0;
		getline(F,s);
		for (int j=0; j<s.size();++j)
		{
			if (s[j]=='J') ++k_J;
			if (s[j]=='E') ++k_E;
		}
		if (k_J>k_E) ++k;
	}
	cout <<k;

}

