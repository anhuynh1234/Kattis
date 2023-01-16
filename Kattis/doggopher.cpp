#include <iostream>
#include <vector>
#include <unordered_set>
#include <cmath>

int main(){
    float xg, yg, xd, yd;
    bool escape = false;
    float xc, yc;
    std::string coord;
    std::string temp_coord;
    std::cin >> xg >> yg >> xd >> yd;
    std::cin.ignore();
    std::vector <std::vector <float>> caves;
    float xca, yca;

    do{
        getline(std::cin, coord);
        if(!coord.empty()){
            for(int i = 0; i < coord.size(); i++){
                if (coord[i] != ' '){
                    temp_coord += coord[i];
                } else if(coord[i] == ' '){
                    xc = std::stof(temp_coord);
                    temp_coord.clear();
                }
            }
            yc = std::stof(temp_coord);
            temp_coord.clear();
            caves.push_back({yc, xc});
            xc = 0; yc = 0;
        }
    }while(!coord.empty());

    for(auto x : caves){
        
        float gop_dist = std::sqrt((std::pow((xg - x[0]), 2) + std::pow((yg - x[1]), 2)));
        float dog_dist = std::sqrt((std::pow((xd - x[0]), 2) + std::pow((yd - x[1]), 2)));
        

        if (gop_dist*2 <= dog_dist){
            escape = 1;
            xca  =x[0]; yca = x[1];
            break;
        }else{
            continue;
        }

    }

    if (escape){
        std::cout << "The gopher can escape through the hole at (" << xca << ',' << yca << ")." << std::endl;
    }else{
        std::cout << "The gopher cannot escape." << std::endl;
    }

}