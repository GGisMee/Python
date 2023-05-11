#include <iostream>

int main(){
    int x; // declare
    x = 12; // funkar också med 
    int y = 12;
    int sum = x+y;

    // std::cout << x+y;
    // std::cout << sum;


    // float age = 5.5;
    double age = 5.5; // funkar med, men bättre för stora decimaltal
    std::cout << age << "\n";

    // char, en bokstav
    char grade = 'A'; // måste dock använda en fnuttar
    std::cout << grade << "\n";

    // boolean
    bool have_eaten = true;
    std::cout << have_eaten << "\n";


    // string
    std:: string name = "Gustav";
    std:: string date = "Friday";
    std:: string food = "pizza";
    std:: string address = "123 fake street";
    std:: cout << "Hello " << name << "\n";

    std::cout << "You are " << age << " years old" << "\n";

    return 0;

    
}
