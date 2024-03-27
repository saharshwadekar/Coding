#include <iostream>
#include <fstream>
#include <chrono>
#include <vector>
using namespace std;
using namespace std::chrono;

void generateRandomArray(const string &fileName, const int size)
{ // generate Random interger array of size write it into file
    ofstream file(fileName);
    if (!file.is_open())
    {
        cerr << "ERROR OPENING :" << fileName << endl;
        exit(EXIT_FAILURE);
    }
    srand(static_cast<unsigned>(time(0)));
    for (int i = 0; i < size; ++i)
        file << rand() % 1000 << " ";
    file.close();
}

void readFile(const string &fileName, int arr[], int size)
{ // Reading file and store values in array
    ifstream file(fileName);
    if (!file.is_open())
    {
        cerr << "ERROR READING :" << fileName << endl;
        exit(EXIT_FAILURE);
    }
    for (int i = 0; i < size; ++i)
        file >> arr[i];
    file.close();
}

// function for heap sort
void heapify(int arr[], int n, int i)
{
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;
    if (right < n && arr[right] > arr[largest])
        largest = right;
    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}
void heapSort(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
      heapify(arr, n, i);

    for (int i = n - 1; i >= 0; i--) {
      swap(arr[0], arr[i]);
      heapify(arr, i, 0);
    }
}

// Function for Quick Sort
int partition(int arr[], int low, int high)
{
    int pivot=arr[high];
    int i=(low-1);
    for(int j=low;j<=high;j++)
    {
        if(arr[j]<pivot)
        {
            i++;
            swap(arr[i],arr[j]);
        }
    }
    swap(arr[i+1],arr[high]);
    return (i+1);
}

void quickSort(int arr[], int low, int high)
{
    if(low<high){
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi-1);
        quickSort(arr, pi+1, high);
    }
}

int main()
{ // defining files names
    const string quickSortFileName = "quickSort.csv";
    const string heapSortFileName = "heapSort.csv";
    const string randomArrayFileName = "randomArrayFile.txt";

    ofstream quickSortFile(quickSortFileName);
    ofstream heapSortFile(heapSortFileName);

    quickSortFile << "Array Size,Time (Quick Sort),Sorted Array" << endl;
    heapSortFile << "Array Size,Time (Heap Sort),Sorted Array" << endl;
    cout << "Array Size"<< "\t"<< "Quick Time"<< "\t"<< "Heap Time"<< "\t" << endl;
    for (int arraySize = 500; arraySize <= 3000; arraySize += 500)
    {
        int numArray[arraySize];
        generateRandomArray(randomArrayFileName, arraySize);
        readFile(randomArrayFileName, numArray, arraySize);
        // quick Sort and measure time
        auto startQuick = high_resolution_clock::now();
        quickSort(numArray,0,arraySize);
        auto stopQuick = high_resolution_clock::now();
        auto durationQuick = duration_cast<microseconds>(stopQuick- startQuick);
        quickSortFile << arraySize << "," << durationQuick.count() << ",";
        for (int i = 0; i < arraySize; ++i)
        { // storing into file
            quickSortFile << numArray[i] << " ";
        }
        quickSortFile << endl;
        // Heap Sort and measure time
        auto startHeap = high_resolution_clock::now();
        heapSort(numArray, arraySize - 1);
        auto stopHeap = high_resolution_clock::now();
        auto durationHeap = duration_cast<microseconds>(stopHeap - startHeap);
        heapSortFile << arraySize << "," << durationHeap.count() << ",";
        for (int i = 0; i < arraySize; ++i)
        {
            heapSortFile << numArray[i] << " ";
        }
        heapSortFile << endl;
        cout << arraySize << "\t\t" << durationQuick.count() << "\t\t" 
        << durationHeap.count() << endl;
    }
    // closing the files where opened
    quickSortFile.close();
    heapSortFile.close();
    return 0;
}