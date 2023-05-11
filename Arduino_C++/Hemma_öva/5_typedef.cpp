#include <iostream>
#include <vector>


// förkortning
// typedef std::vector<std::pair<std::string, int>> pairlist_t;

typedef std::string text_t;
typedef int number_t;

// annan metod

// using text_t = std::string;
// using number_t = int;

int main(){
    text_t name = "Gustav";
    number_t age = 16;
    std::cout<<name<<" thats "<< age;


    return 0;
}