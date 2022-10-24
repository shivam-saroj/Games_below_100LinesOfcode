#include<iostream>
#include<vector>
using namespace std;

bool check_guess(int guess, int actual) {

    if (actual == guess) {
        cout << "Wohhoooo!!!! You win!\n";
        return 1;
    } else {
        if (guess > actual) {
            cout << "Uh oh! Guess lower\n";
        } else {
            cout << "Uh oh! Guess higher\n";
        } 
        return 0;
    }
}


int main() {
    
    int answer = rand() % 100;

    int guess;

    do {
        cout << "Enter guess : ";
        cin >> guess;
    } while(!check_guess(guess, answer));

}
