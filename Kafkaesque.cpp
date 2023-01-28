#include <iostream>
#include <vector>
#include <algorithm>
// #include <queue>


int main(){
    int k;
    int clerk, traverse = 0;
    std::vector <int> clerks, order;

    std::cin >> k;

    for (int i = 0; i < k; i++){
        std::cin >> clerk;
        order.push_back(clerk);
        clerks.push_back(clerk);
    }

    std::sort(order.begin(), order.end(), std::greater<int>());

    while (order.size() > 0){
        int smallest = std::distance(clerks.begin(), std::find(clerks.begin(), clerks.end(), order[order.size()-1]));
        order.pop_back();
        if (order.size() > 0){
            while (std::distance(clerks.begin(), std::find(clerks.begin(), clerks.end(), order[order.size()-1])) > smallest){
                smallest = std::distance(clerks.begin(), std::find(clerks.begin(), clerks.end(), order[order.size()-1]));
                order.pop_back();
                if (order.size() == 0){
                    break;
                }
            }
        }
        traverse++; 
    }
    std::cout << traverse << std::endl;
   
}