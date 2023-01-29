#include <iostream>
#include <vector>
#include <cmath>


int main(){
    double times, area[100];
    std::cin >> times;
    for(int i = 0; i < times; i++){
        int sides;
        std::vector <std::vector <double>> coords;
        std::vector <double> coord;
        std::cin >> sides;
        double x, y;
        for(int j = 0; j < sides; j++){
            std::cin >> x >> y;
            coord.push_back(x);
            coord.push_back(y);
            coords.push_back(coord);
            coord.clear();
        }
        // x = coords[0][0]; y = coords[0][1];
        double add = coords[0][1] * coords[coords.size()-1][0], subtract = coords[0][0] * coords[coords.size()-1][1]; 

        for(int m = 0; m < coords.size()-1; m ++){
            add += coords[m][0] * coords[m+1][1];
            subtract += coords[m+1][0] * coords[m][1];
        }
        area[i] = (add - subtract)/2;
        
        coords.clear();
    }
    for(int n =0; n < times; n ++){
        std::cout << area[n] << std::endl;
    }
}