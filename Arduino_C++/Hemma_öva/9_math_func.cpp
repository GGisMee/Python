#include <iostream>
#include <cmath>
using namespace std;

int main(){
    double x = 3;
    double y = 4;
    double z;
    // största värdet
    cout<<"\n"<<max(x,y)<<"\n";

    // minsta värdet
    cout<<min(x,y)<<"\n";
    
    // upphöjt och 
    cout<<pow(2,4)<<"\n"; // 4^2
    cout<<sqrt(9)<<"\n";
    // alt 4**2, 9**(1/2)

    // absolut belopp
    cout<<abs(-8)<<"\n";

    // avrunda
    cout<<round(3.4)<<"\n";
    // avrunda upp
    cout<<ceil(3.4)<<"\n";
    //avrunda ned
    cout<<floor(3.4)<<"\n";



};