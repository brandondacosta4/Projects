#include <iostream>
#include <string>
#include <vector>
#include <time.h>

using namespace std;

bool check_true(string check){
    if(check == "y" || check == "Y"){
        return true;
    }

    if(check == "n" || check == "N"){
        return false;
    }

}

int random_num(int start_range, int end_range){
    return rand() % end_range + start_range;

}

int main(){
    
    cout << "\nWelcome to the strong password generator!\n";

    cout << "\nPlease enter the desired password length: ";
    int length;
    cin >> length;

    string answer;
    cout << "\nWould you like to include uppercase letters (Y/N)? ";
    cin >> answer;
    bool include_uppercase_letters = check_true(answer);

    cout << "\nWould you like to include lowercase letters (Y/N)? ";
    cin >> answer;
    bool include_lowercase_letters = check_true(answer);

    cout << "\nWould you like to include numbers (Y/N)? ";
    cin >> answer;
    bool include_numbers = check_true(answer);

    cout << "\nWould you like to include symbols (Y/N)? ";
    cin >> answer;
    bool include_symbols = check_true(answer);


    string upper_letters[26] = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"};
    string lower_letters[26] = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"};
    string num[10] = {"1","2","3","4","5","6","7","8","9","0"};
    string symbols[8] = {"!", "@", "#", "$", "%", "^", "&", "*"};


    vector <string> password;

    srand(time(NULL));
    for(int i = 0; i < length; i++){
        int option = random_num(1,4);

        if (option == 1){
            if(include_uppercase_letters == false){
                i = i-1;
                
            }
            else{
                password.push_back(upper_letters[random_num(0, 25)]);
            }
        }

        else if(option == 2){
            if(include_lowercase_letters == false){
                i = i-1;
                
            }
            else{
                password.push_back(lower_letters[random_num(0, 25)]);
            }
        }

        else if(option == 3){
            if(include_numbers == false){
                i = i-1;
                
            }
            else{
                password.push_back(num[random_num(0, 9)]);
            }

        }

        else if(option == 4){
            if(include_symbols == false){
                i = i-1;
                
            }
            else{
                password.push_back(symbols[random_num(0, 7)]);
            }
        }
    }
    
    cout << "\nYour generated password is: ";

    for(int i = 0; i < password.size(); i++){
        cout << password[i];
    }
}
