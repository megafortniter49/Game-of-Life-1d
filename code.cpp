#include <iostream>
#include <vector>
#include <chrono>
#include <thread>
#include <cstdlib>
#include <limits>

using namespace std;

void printWorld(const vector<bool>& world) {
    for (bool cell : world) {
        cout << (cell ? '*' : ' ') << " ";
    }
    cout << endl;
}

vector<bool> generateNextState(const vector<bool>& current) {
    vector<bool> next(current.size());
    int size = current.size();
    for (int i = 0; i < size; i++) {
        int leftNeighbor = i - 1 < 0 ? size - 1 : i - 1;
        int rightNeighbor = i + 1 >= size ? 0 : i + 1;
        int aliveNeighbors = current[leftNeighbor] + current[rightNeighbor];

        if (current[i]) {
            next[i] = aliveNeighbors == 1;
        }
        else {
            next[i] = aliveNeighbors == 1;
        }
    }
    return next;
}

void clearCin() {
    cin.clear(); // Восстанавливаем cin после ошибки ввода
    cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Удаляем лишние символы из входного буфера
}

int getIntInput(const string& prompt) {
    int value;
    while (true) {
        cout << prompt;
        if (cin >> value) {
            clearCin(); // Очищаем cin для будущего использования
            return value;
        }
        else {
            cout << "Please enter a valid integer." << endl;
            clearCin(); // Очищаем cin после неверного ввода
        }
    }
}

bool getBoolInput(const string& prompt) {
    char choice;
    while (true) {
        cout << prompt;
        if (cin >> choice) {
            clearCin(); // Очищаем cin для будущего использования
            if (choice == 'y' || choice == 'Y') return true;
            if (choice == 'n' || choice == 'N') return false;
        }
        cout << "Please enter 'y' for yes or 'n' for no." << endl;
        clearCin(); // Очищаем cin после неверного ввода
    }
}

void initializeWorld(vector<bool>& world) {
    bool manualInput = getBoolInput("Do you want to enter the live cells manually? (y/n): ");
    if (manualInput) {
        cout << "Enter the numbers of cells that are alive (1-indexed), followed by -1 to end: ";
        int cellNumber;
        while (true) {
            cellNumber = getIntInput("");
            if (cellNumber == -1) break;
            if (cellNumber > 0 && cellNumber <= world.size()) {
                world[cellNumber - 1] = true;
            }
            else {
                cout << "Invalid cell number, please enter a number between 1 and " << world.size() << ": ";
            }
        }
    }
    else {
        for (int i = 0; i < world.size(); i++) {
            world[i] = rand() % 2;
        }
    }
}

void runSimulation(int worldSize, int generations) {
    vector<bool> world(worldSize);
    initializeWorld(world);

    cout << "Initial World:" << endl;
    printWorld(world);

    for (int gen = 0; gen < generations; gen++) {
        world = generateNextState(world);
        printWorld(world);
        this_thread::sleep_for(chrono::milliseconds(500));
    }
}

int main() {
    srand(time(nullptr));

    int worldSize = getIntInput("Enter the length of the world: ");
    int generations = getIntInput("Enter the number of generations: ");

    do {
        runSimulation(worldSize, generations);
    } while (getBoolInput("Start a new simulation? (y/n): "));

    return 0;
}
