// Автор: М. Нехорошева

#include <iostream>
#include <fstream>
using namespace std;

int main() 
{
	fstream F;  //открываем файл в режиме чтения  
	F.open("24s.txt");
	string s;
	getline(F,s);
	int arr[26]={0};
	for (int i=0; i<s.size()-2;++i)
	{
		if (s[i]==s[i+2])
			++arr[s[i+1]-'A'];
	}
	int m=0;
	for (int i=0; i<26;++i)
	{
		if(arr[i]>arr[m])
			m=i;

		cout<<(char)(i+'A')<<"  "<<arr[i]<<endl;
	}
		char d=m+'A';
		cout<<d;	
}
