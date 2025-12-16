// Автор: М. Нехорошева

#include <iostream>
#include <fstream>
using namespace std;

int main (){
	fstream fu;
	fu.open("24-191.txt");
	string s;
	getline (fu,s);
//	cout<<s;
	int a, f, che, m;
	for(int i=0; i<s.size(); i++){
		if(s[i]=='A'){
			a=1;
			f=0;
			che=0;
		}
		if(a==1){
			che++;
			if(s[i]=='F')
				f++;
			if(s[i]=='B'){
				a=0;
				if(f==2){
					f=0;
					if(che>=20){
						m++;
						che=0;	
					}
					else
						che=0;
				}
			}	
		}
	}
	cout<<m;
}
