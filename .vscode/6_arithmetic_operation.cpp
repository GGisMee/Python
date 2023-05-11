# include <iostream>

int main(){
    int students = 20;

    // +-
    students+=1;
    students++;
    students-=1;
    students--;


    // /*
    students*=2;
    students/=3;


    // det som blir över
    int remainder = students % 2;

    std::cout << students << "\n";
    std::cout << remainder;

    if (students != 1){
        std::cout << remainder<<"d";
    }

    return 0;
}