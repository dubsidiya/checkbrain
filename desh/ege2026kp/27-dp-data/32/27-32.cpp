// Автор: М. Нехорошева

#include <iostream>
#include <fstream>
#include <vector>
int main()
{
	const char* path = "27-32b.txt";
	std::ifstream f1(path);
	int n;
	f1 >> n;
	
	std::vector<int> rems(11, 0);
	
	while(n--)
	{
		std::vector<int> new_rems(11, 999999999);
		for(int _k=3; _k--;)
		{
			int a;
			f1 >> a;
			
			for(auto r : rems)
			{
				int nr = r + a;
				new_rems[nr % 11] = std::min(new_rems[nr % 11], nr);
			}
			
		}
		
		rems = new_rems;
	}
	
	std::cout << rems[0] << std::endl;
}
