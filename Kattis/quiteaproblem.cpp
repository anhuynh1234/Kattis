#include <iostream>
#include <string>
#include <vector>
#include <bits/stdc++.h>
#include <cstring>

int main(){

    std::string lines;
    std::vector <std::string> results;
    do{
        getline(std::cin, lines);
        if (!lines.empty()){
            std::transform(lines.begin(), lines.end(), lines.begin(), ::tolower);
            if (lines.find("problem") != std::string::npos){
                results.push_back("yes");
            }else{
                results.push_back("no");
            }
        }
    } while(!lines.empty());


    for(std::string x : results){
        std::cout << x << std::endl; 
    }

}

