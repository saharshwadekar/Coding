#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <chrono>

using namespace std;
using namespace std::chrono;

void generateAndSaveRandomNumbers(const string& fileName, int size) {
    ofstream file(fileName);
    if (!file.is_open()) {
        cerr << "Error opening file for writing: " << fileName << endl;
        exit(EXIT_FAILURE);
    }

    srand(static_cast<unsigned>(time(0)));
    for (int i = 0; i < size; ++i) {
        file << rand() % 1000 << " ";
    }

    file.close();
}

void readNumbersFromFile(const string& fileName, int arr[], int size) {
    ifstream file(fileName);
    if (!file.is_open()) {
        cerr << "Error opening file for reading: " << fileName << endl;
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < size; ++i) {
        file >> arr[i];
    }

    file.close();
}

void bubbleSort(int arr[], int size) {
    for (int i = 0; i < size - 1; ++i) {
        for (int j = 0; j < size - i - 1; ++j) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

void selectionSort(int arr[], int size) {
    for (int i = 0; i < size - 1; ++i) {
        int minIndex = i;
        for (int j = i + 1; j < size; ++j) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        swap(arr[i], arr[minIndex]);
    }
}

int main() {
    const string inputFileName = "random_numbers.txt";
    const string bubbleSortFileName = "bubble_sort_result.csv";
    const string selectionSortFileName = "selection_sort_result.csv";
    const int maxArraySize = 1000; // Set the maximum array size for testing
    const int stepSize = 50;      // Set the step size for increasing array size

    ofstream bubbleSortFile(bubbleSortFileName);
    ofstream selectionSortFile(selectionSortFileName);

    bubbleSortFile << "Array Size,Time (Bubble Sort)" << endl;
    selectionSortFile << "Array Size,Time (Selection Sort)" << endl;

    for (int arraySize = stepSize; arraySize <= maxArraySize; arraySize += stepSize) {
        // Generate and save random numbers
        generateAndSaveRandomNumbers(inputFileName, arraySize);

        // Read numbers from the file
        int numbers[arraySize];
        readNumbersFromFile(inputFileName, numbers, arraySize);

        // Bubble Sort and measure time
        auto startBubble = high_resolution_clock::now();
        bubbleSort(numbers, arraySize);
        auto stopBubble = high_resolution_clock::now();
        auto durationBubble = duration_cast<microseconds>(stopBubble - startBubble);
        bubbleSortFile << arraySize << "," << durationBubble.count() << ",";
        for (int i = 0; i < arraySize; ++i)
        {
            bubbleSortFile << numbers[i] << " ";
        }
        bubbleSortFile << endl;

        // Read numbers from the file again
        readNumbersFromFile(inputFileName, numbers, arraySize);

        // Selection Sort and measure time
        auto startSelection = high_resolution_clock::now();
        selectionSort(numbers, arraySize);
        auto stopSelection = high_resolution_clock::now();
        auto durationSelection = duration_cast<microseconds>(stopSelection - startSelection);
        selectionSortFile << arraySize << "," << durationSelection.count() << ",";
        for (int i = 0; i < arraySize; ++i)
        {
            selectionSortFile << numbers[i] << " ";
        }
        selectionSortFile << endl;
    }

    bubbleSortFile.close();
    selectionSortFile.close();

    cout << "Sorting and data collection completed. Results saved in CSV files." << endl;

    return 0;
}
