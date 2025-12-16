// Автор: М. Нехорошева

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main() 
{
	fstream F;  //открываем файл в режиме чтения  
	F.open("24-157.txt");
	string s;
	vector <int> v;
	int mk=0,k;
	getline(F,s);
	for (int i=0;i<s.size()-1;++i)
	{
		if (s[i]=='Q' && s[i+1]=='W')
 			{
 				v.push_back(k);
 				k=1;
			 }
   		else 
			++k;			
	}
	cout<<*max_element(v.begin(),v.end());
}
