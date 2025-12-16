// Автор: М. Нехорошева

#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;

int main() 
{
	ifstream F;  //открываем файл в режиме чтения  
	F.open("24-10.txt");
	int k=0 ;
	//string c;
	long long int c,max_E=0;
	for (;!F.eof();)
	{
		//getline(F,c);
		++k;
		//int f=atoi(c.c_str());
		F>>c;
		max_E+=c;
	}
	cout <<float() max_E/k*1.0;
	F.close ();	

}


