#include <iostream>
namespace first{
    int x = 1;
}

namespace two{
    int x = 2;
}

int main(){
    using std::string;
    // alt
    //using namespace two;

    // för att slippa specifisiera i kod
    string y = "hello";

    // std::string x = "hello";

    std::cout << two::x << " and " << y;





    return 0;
} 