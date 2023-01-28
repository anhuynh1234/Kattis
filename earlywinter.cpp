#include <iostream>



int main(){
    int n, dm;
    std::cin >> n >> dm;
    int days[n], k;
    bool early = false;

    for (int i = 0; i < n; i++){
        std::cin >> days[i];
    }

    int j = 0;
    for (j; j < n; j++){
        if (days[j] > dm){
            continue;
        }else if (days[j] <= dm){
            early = 1;
            break;
        }
    }

    if (early){
        std::cout << "It hadn't snowed this early in " << j <<" years!" << std::endl;
    }else if(!early){
        std::cout << "It had never snowed this early!" << std::endl;
    }
}