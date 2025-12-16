// Автор: М. Нехорошева

#include <iostream>
#include <fstream>
using namespace std;

int main() 
{
	fstream F;  //открываем файл в режиме чтения  
	F.open("24-j9.txt");
	string s;
	getline(F,s);
	int k=0;
	for (int i=0, j=s.size()-1;i<j;++i,--j)
		if(s[i]==s[j])
			++k;
	cout<<k;
}
