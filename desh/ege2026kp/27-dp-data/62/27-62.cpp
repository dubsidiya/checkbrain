// Автор: М. Нехорошева

#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cmath>
using namespace std;
int main()
{
	fstream f;
	f.open("27-62b.txt");
	vector<int> v;
	for (int n; f >> n; v.push_back(n)); 
	sort(v.begin()+1, v.end());
	int maxr = 0,z;
	for (int d = 1; d < 100; d++)
	{
		for (int i = 0; i < v.size(); i++)
			for (int a = v[i], lmax = 1 ;; a = a + d, lmax++, maxr = max(maxr, lmax));
	}
	cout << maxr<<"  ";
}


















