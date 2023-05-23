#include <iostream>
using namespace std;

int main(){
    string name;
    int age;
    cout<<"What is your full name?: ";
    // cin>>name; // tar inputen och lägger den i name
    // cin<<name funkar ej om man vill ha en string med mellanslag. Använd då istället getline(cin, name);
    getline(cin, name);

    cout<<"What is your age?: ";
    cin>>age; // tar inputen och lägger den i name

    cout<<"Hello "<<age<<" y.o "<<name<<".\n";

    return 0;
}