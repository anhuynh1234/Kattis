#include <iostream>
#include <iomanip>

int main(){
    float n, k;
    double d, s, average;

    std::cin >> n >> k >> d >> s;

    average = double((d*n-k*s)/(n-k));

    if (average >= 0 && average <= 100){
        std::cout << std::setprecision(11) << average << std::endl; 
    }else if (average < 0 || average > 100 ){
        std::cout << "impossible" << std::endl;
    }
    


}