// Автор: М. Нехорошева

#include<bits/stdc++.h>
using namespace std;
int main()
{
		for(long long int i=123042593 ; i<124*1e9; i+=4013){
		string s="";
		s=to_string(i);
		if(s.find("123")==0 && s[4]=='4' && s.rfind("5679")==s.size()-4)
		{
			cout<<i<<"  "<<i/4013<<endl;
		}
	}
}
