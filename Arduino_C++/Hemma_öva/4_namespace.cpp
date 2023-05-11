#include <iostream>
namespace first{
    int x = 1;
}

namespace two{
    int x = 2;
}

int main(){
    using std::string;
    using namespace first;
    // för att slippa specifisiera i kod
    string y = "hello";

    // std::string x = "hello";

    std::cout << x << " and " << y;





    return 0;
} 