#include <iostream>
#include <vector>
#include <algorithm>


int main(){
    int n, m;
    std::vector <int> t, l;
    std::cin >> n >> m;

    int tim, len;

    for(int i = 0; i < n; i++){
        std::cin >> tim;
        t.push_back(tim);
    }

    for(int j = 0; j < m; j++){
        std::cin >> len;
        l.push_back(len);
    }

    std::sort(t.begin(), t.end());
    std::sort(l.begin(), l.end());

    int finished = 0;

    while(!t.empty() & !l.empty()){
        if(l[l.size()-1] >= t[t.size()-1]){
            t.pop_back();
            l.pop_back();
            finished++;        
        }else if(t[t.size()-1] > l[l.size()-1]){
            t.pop_back();
        }
    }

    std::cout << finished << std::endl;


}