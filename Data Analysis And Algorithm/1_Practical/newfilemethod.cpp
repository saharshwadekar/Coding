#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <chrono>

using namespace std;
using namespace std::chrono;

// function to generate randome number and save it in file
void generateAndSaveRandomNumbers(const string &fileName, int size)
{
    ofstream file(fileName); // file open for writing
    if (!file.is_open())
    { // Open file error detection
        cerr << "Error opening file for writing: " << fileName << endl;
        exit(EXIT_FAILURE); // exit with failure status
    }

    srand(static_cast<unsigned>(time(0))); // seed assigned
    for (int i = 0; i < size; ++i)
    {                                 // store to the file
        file << rand() % 1000 << " "; // random(0 to 999) generated
    }

    file.close(); // closing the file
}

// Function to read numbers from a file and save them in an array
void readNumbersFromFile(const string &fileName, int arr[], int size)
{
    ifstream file(fileName); // open file for reading
    if (!file.is_open())
    { // Open file error detection
        cerr << "Error opening file for reading: " << fileName << endl;
        exit(EXIT_FAILURE); // exit with failure status
    }

    for (int i = 0; i < size; ++i)
    {
        file >> arr[i]; // inserting data to the array form file
    }

    file.close(); // closing file
}

// funciton of an bubble sort implementation
void bubbleSort(int arr[], int size)
{
    for (int i = 0; i < size - 1; ++i)
    {
        int flag = false;
        for (int j = 0; j < size - i - 1; ++j)
        {
            if (arr[j] > arr[j + 1])
            {
                swap(arr[j], arr[j + 1]);
                flag = true;
            }
        }
        if (!flag)
            break;
    }
}
// funciton of an seleciton sort implementation
void selectionSort(int arr[], int size)
{
    for (int i = 0; i < size - 1; ++i)
    {
        int minIndex = i; // getting least value array index
        for (int j = i + 1; j < size; ++j)
        {
            if (arr[j] < arr[minIndex])
            {
                minIndex = j;
            }
        }
        swap(arr[i], arr[minIndex]); // lowest put forward
    }
}

int main()
{
    const string inputFileName = "random_numbers.txt";
    const string bubbleSortFileName = "bubble_sort_result.csv";
    const string selectionSortFileName = "selection_sort_result.csv";
    const int maxArraySize = 1000; // Set the maximum array size for testing
    const int stepSize = 50;       // Set the step size for increasing array size

    // opening respective files
    ofstream bubbleSortFile(bubbleSortFileName);
    ofstream selectionSortFile(selectionSortFileName);

    bubbleSortFile << "Array Size,Time (Bubble Sort), Sorted Array" << endl;
    selectionSortFile << "Array Size,Time (Selection Sort), Sorted Array" << endl;

    // Impliment stepwise manner array of number increase
    for (int arraySize = stepSize; arraySize <= maxArraySize; arraySize += stepSize)
    {
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
        { // storing into file
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

    // closing the files where opened
    bubbleSortFile.close();
    selectionSortFile.close();

    // successfull message to terminal
    cout << "Sorting and data collection completed. Results saved in CSV files." << endl;

    return 0;
}
