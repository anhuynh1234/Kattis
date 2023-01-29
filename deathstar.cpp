#include <iostream>
#include <vector>
#include <cmath>

std::vector <int> forward(int d, int h, int m);
std::vector <int> backward(int d, int h, int m);


int main(){
    int cases; 
    std::cin >> cases;
    std::vector <std::vector <int>> times;
    for(int i = 0; i < cases; i++){
        char move;
        int d, h, m;
        std::vector <int> time;
        std::cin >> move >> d >>h >> m;
        if(move == 'F'){
            time = forward(d, h, m);
        }else if(move == 'B'){
            time = backward(d, h, m);
        }
        times.push_back(time);
        time.clear();
    }

    for(auto x:times){
        std::cout << x[0] << ' ' << x[1] << std::endl;
    }

}

std::vector <int> forward(int d, int h, int m){
    m += d%60; 
    if(m >= 60){
        m -= 60;
        h++;
    }
    h += std::floor(d/60);
    while(h >= 24){
        h -= 24;
    }
    return {h, m};
}

std::vector <int> backward(int d, int h, int m){
    m -=  d%60;
    if(m < 0){
        m += 60;
        h--;
    } 
    h -= std::floor(d/60);
    if(h < 0){
        h += 24;
    }
    return {h, m};
}