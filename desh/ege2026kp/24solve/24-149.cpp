// Автор: М. Нехорошева

#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
	ifstream f("24-s2.txt");
	string s;
	getline(f,s);
	vector <int> ss(26);
	int k=0, m=0;
	for (int i=1;i<s.size();++i)
		if(s[i-1]=='A')
			ss[s[i]-'A']++;
//	int m=0;
	for(int i=0; i<ss.size();++i)
		cout<<(char)(i+'A')<<"  "<<ss[i]<<endl;
	cout<<*max_element(ss.begin(), ss.end());
}
