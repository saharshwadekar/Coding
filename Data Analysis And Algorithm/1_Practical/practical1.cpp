#include <iostream>
#include <fstream>
#include <chrono>

using namespace std;
using namespace std::chrono;

void generateRandomArray(const string &fileName, const int size)
{   // generate Random interger array of size write it into file
    ofstream file(fileName);
    if (!file.is_open())
    {
        cerr << "ERROR OPENING :" << fileName << endl;
        exit(EXIT_FAILURE);
    }
    srand(static_cast<unsigned>(time(0)));
    for (int i = 0; i < size; ++i)
    {
        file << rand() % 1000 << " ";
    }
    file.close();
}

void readFile(const string &fileName, int arr[], int size)
{       // Reading file and store values in array
    ifstream file(fileName);
    if (!file.is_open())
    {
        cerr << "ERROR READING :" << fileName << endl;
        exit(EXIT_FAILURE);
    }
    for (int i = 0; i < size; ++i)
    {
        file >> arr[i];
    }
    file.close();
}

void bubbleSort(int arr[], int size)
{
    // Sorting Bubble
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
// Function for selection Sort
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
{   // defining files names
    // const string inputFile = "inputfile.txt";
    const string bubbleSortFileName = "bubbleSort.csv";
    const string selectionSortFileName = "selectionSort.csv";
    const string randomArrayFileName = "randomArrayFile.txt";
    // // generate size
    // // const int randomSize = (rand() % 10) + 1;
    // // int sizeArray[randomSize];

    // // generateRandomArray(inputFile, randomSize);
    // // readFile(inputFile, sizeArray, randomSize);

    ofstream bubbleSortFile(bubbleSortFileName);
    ofstream selectionSortFile(selectionSortFileName);

    bubbleSortFile << "Array Size,Time (Bubble Sort), Sorted Array" << endl;
    selectionSortFile << "Array Size,Time (Selection Sort), Sorted Array" << endl;
    cout << "Array Size" << "\t" << "Bubble Time" << "\t" 
         << "Selection Time" << "\t" << endl;
    // // for (auto arraySize : sizeArray)
    for(int arraySize = 500 ; arraySize <= 3000 ; arraySize += 500)
    {
        int numArray[arraySize];

        generateRandomArray(randomArrayFileName, arraySize);
        readFile(randomArrayFileName, numArray, arraySize);

        // Bubble Sort and measure time
        auto startBubble = high_resolution_clock::now();
        bubbleSort(numArray, arraySize);
        auto stopBubble = high_resolution_clock::now();
        auto durationBubble = duration_cast<microseconds>(stopBubble - startBubble);
        bubbleSortFile << arraySize << "," << durationBubble.count() << ",";
        for (int i = 0; i < arraySize; ++i)
        { // storing into file
            bubbleSortFile << numArray[i] << " ";
        }
        bubbleSortFile << endl;

        // Selection Sort and measure time
        auto startSelection = high_resolution_clock::now();
        selectionSort(numArray, arraySize);
        auto stopSelection = high_resolution_clock::now();
        auto durationSelection = duration_cast<microseconds>(stopSelection - startSelection);
        selectionSortFile << arraySize << "," << durationSelection.count() << ",";
        for (int i = 0; i < arraySize; ++i)
        {
            selectionSortFile << numArray[i] << " ";
        }
        selectionSortFile << endl;

        cout << arraySize << "\t\t" << durationBubble.count() << "\t\t" 
             << durationSelection.count() << endl;
    }

    // closing the files where opened
    bubbleSortFile.close();
    selectionSortFile.close();

    return 0;
}