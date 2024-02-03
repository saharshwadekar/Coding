#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <chrono>

using namespace std;
using namespace std::chrono;

// Function to generate random numbers and store them in a file
void generateAndSaveRandomNumbers(const string &fileName, int size)
{
    ofstream file(fileName);
    if (!file.is_open())
    {
        cerr << "Error opening file for writing: " << fileName << endl;
        exit(EXIT_FAILURE);
    }

    srand(static_cast<unsigned>(time(0)));
    for (int i = 0; i < size; ++i)
    {
        file << rand() % 1000 << " "; // Assuming random numbers between 0 and 999
    }

    file.close();
}

// Function to read numbers from a file and save them in an array
void readNumbersFromFile(const string &fileName, int arr[], int size)
{
    ifstream file(fileName);
    if (!file.is_open())
    {
        cerr << "Error opening file for reading: " << fileName << endl;
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < size; ++i)
    {
        file >> arr[i];
    }

    file.close();
}

// Bubble Sort implementation
void bubbleSort(int arr[], int size)
{
    for (int i = 0; i < size - 1; ++i)
    {
        for (int j = 0; j < size - i - 1; ++j)
        {
            if (arr[j] > arr[j + 1])
            {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

// Selection Sort implementation
void selectionSort(int arr[], int size)
{
    for (int i = 0; i < size - 1; ++i)
    {
        int minIndex = i;
        for (int j = i + 1; j < size; ++j)
        {
            if (arr[j] < arr[minIndex])
            {
                minIndex = j;
            }
        }
        swap(arr[i], arr[minIndex]);
    }
}

int main()
{
    const string inputFileName = "random_numbers.txt";
    const string bubbleSortFileName = "bubble_sort_result.txt";
    const string selectionSortFileName = "selection_sort_result.txt";
    const int arraySize = 1000; // Change the size as needed

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

    // Save sorted numbers and time taken for Bubble Sort
    ofstream bubbleSortFile(bubbleSortFileName);
    for (int i = 0; i < arraySize; ++i)
    {
        bubbleSortFile << numbers[i] << " ";
    }
    bubbleSortFile << "\nTime taken for Bubble Sort: " << durationBubble.count() << " microseconds";
    bubbleSortFile.close();

    // Read numbers from the file again
    readNumbersFromFile(inputFileName, numbers, arraySize);

    // Selection Sort and measure time
    auto startSelection = high_resolution_clock::now();
    selectionSort(numbers, arraySize);
    auto stopSelection = high_resolution_clock::now();
    auto durationSelection = duration_cast<microseconds>(stopSelection - startSelection);

    // Save sorted numbers and time taken for Selection Sort
    ofstream selectionSortFile(selectionSortFileName);
    for (int i = 0; i < arraySize; ++i)
    {
        selectionSortFile << numbers[i] << " ";
    }
    selectionSortFile << "\nTime taken for Selection Sort: " << durationSelection.count() << " microseconds";
    selectionSortFile.close();

    cout << "Sorting completed. Results saved in files." << endl;

    return 0;
}
