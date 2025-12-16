// Автор: М. Нехорошева

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void print20(int num) {
	char str[128];
	
	int i = 127;
	
	do {
		int rem = num % 20;
		str[--i] = rem < 10 ? '0' + rem : 'A' - 10 + rem;
		
		num /= 20;
	} while(num > 0);
	
	cout << str + i << endl;
}

int main() {
	ifstream in("24-268.txt");
	
	int maxnum = 0;
	
	int num = 0;
	
	for (char c; in >> c; ) {
		if (num == 0 && c == '0')
			num = -1;
		
		if (c >= '0' && c <= '9') {
			num = num * 20 + c - '0';
		} else if (c >= 'A' && c <= 'J') {
			num = num * 20 + c - ('A' - 10);
		} else {
			if (num > 0 && (num & 0x1) == 0) {
				maxnum = max(maxnum, num);
			}
			
			num = 0;
		}
	}
	
	if (num > 0 && (num & 0x1) == 0) {
		maxnum = max(maxnum, num);
	}
	
	print20(maxnum);
	
	in.close();
}
