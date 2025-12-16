// Автор: М. Нехорошева

#include <iostream>
#include <fstream>
using namespace std;
int main() 
{
	ifstream F;  //открываем файл в режиме чтения  
	F.open("k7c-1.txt");
	string s;
	getline(F,s);
	int k=0;
	for (int i=0;i<s.size()-2;++i)
	{
		if(s[i]=='B' || s[i]=='C'|| s[i]=='D' )// 1-й символ - один из символов B, C или D;
			 if ((s[i+1]=='B' || s[i+1]=='E'|| s[i+1]=='D')&& s[i]!=s[i+1])
			 //2-й символ - один из символов B, D, E, который не совпадает с первым; 
				if ((s[i+2]=='B' || s[i+2]=='E'|| s[i+2]=='C')&& s[i+2]!=s[i+1])
				//3-й символ - один из символов B, C, E, который не совпадает со вторым.
	  		   		++k;
	}
	cout <<k;
	F.close ();	
}


