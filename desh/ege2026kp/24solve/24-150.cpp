// Автор: М. Нехорошева

#include <iostream>
#include <fstream>
using namespace std;

int main() 
{
	fstream F;  //открываем файл в режиме чтения  
	F.open("24-s1.txt");
	string s;
	int k=0;
	getline(F,s);
	for (int i=0,j=s.size()-1; i<j;++i,--j)
			if (s[i]==s[j]) 
				++k;
	cout <<k;
}

