// Автор: М. Нехорошева

#include <iostream>
#include <fstream>
using namespace std;

int main() 
{
	fstream F;  //открываем файл в режиме чтения  
	F.open("24-s1.txt");
	string s;
	int k_j=0;
	for(;!F.eof();)
	{
		int j,e;
		j=e=0;
		getline(F,s);
		for(int i=0;i<s.size();++i)
			{
				if(s[i]=='J') ++j;
				if(s[i]=='E') ++e;	
			}
		if (j>e) ++k_j;			
	}
	cout <<k_j;

}
