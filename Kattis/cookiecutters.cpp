#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <unordered_set>
#include <algorithm>


int main(){
    int n;
    std::string word, instance, name, course;
    std::vector <std::string> words;
    std::cin >> n;
    std::map <std::string, std::unordered_set <std::string>> reg;
    std::cin.ignore();

    do{
        getline(std::cin, instance);
        
        if (!instance.empty()){
            for (int i = 0; i < instance.length(); i++){
                switch (instance[i]){
                    case ' ':
                        words.push_back(word);
                        word.clear();
                    default:
                        word += instance[i];
                }
            }
            std::remove(word.begin(), word.end(), ' ');
            course = word;
            word.clear();
            name = words[0] + words[1];

            if (reg.find(course) != reg.end()){
                reg[course].insert(name);
            }else if (!reg.count(course)){
                std::unordered_set <std::string> names = {name};
                reg.insert({course, names});
            }
            words.clear();

        }
    
    }while(!instance.empty());

    for (auto j : reg){
        std::string key = j.first;
        int length = (j.second).size(); 

        std::cout << key << ' ' << length << std::endl;
    }

}