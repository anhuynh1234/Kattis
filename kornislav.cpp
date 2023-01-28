#include <iostream>
#include <algorithm>
#include <vector>


int main(){
    int a, b, c, d;
    std::vector <int> sides;
    std::cin >> a >> b >> c >> d;
    sides.push_back(a);
    sides.push_back(b);
    sides.push_back(c);
    sides.push_back(d);

    std::sort(sides.begin(), sides.end());

    std::cout << sides[0]*sides[2] << std::endl;
}