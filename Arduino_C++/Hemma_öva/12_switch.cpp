#include <iostream>
using namespace std;
// alternativ till många else if
int main(){
    int inp;
    cout<<"Enter input: ";
    cin>>inp;
    switch (inp)
    {
    case 1:
        cout<<"inp = 1"<<"\n";
        break;
    case 2:
        cout<<"inp = 2"<<"\n";
        break;
    case 3:
        cout<<"inp = 3"<<"\n";
        break;
    case 4:
        cout<<"inp = 4"<<"\n";
        break;
    case 5:
        cout<<"inp = 5"<<"\n";
        break;
    default:
        cout<<"other"<<"\n";
    
    return 0;
    }
}