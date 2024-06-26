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
    {
        file << rand() % 1000 << " ";
    }
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
    {
        file >> arr[i];
    }
    file.close();
}
// function for INSERTION Sort
void insertionSort(int arr[], int size)
{
    for (int i = 1; i < size; ++i)
    {
        int key = arr[i];
        int j = i;
        while (--j >= 0 && arr[j] > key)
            arr[j + 1] = arr[j];
        arr[j + 1] = key;
    }
}

void merge(int arr[], int l, int m, int r)
{
    int n1 = m-l+1;
    int n2 = r-m;
    int* L = new int[n1];
    int* R = new int[n2];

    for(int i=0; i<n1; ++i)
        L[i] = arr[l+i];
    for(int i=0; i<n2; ++i)
        R[i] = arr[m+1+i];

    int i = 0, j = 0, k = l;
    while(i < n1 && j < n2)
    {
        if(L[i] <= R[j])
            arr[k++] = L[i++];
        else    
            arr[k++] = R[j++];
    }

    while(i < n1)
        arr[k++] = L[i++];

    while(j < n2)
        arr[k++] = R[j++];

    delete[] L;
    delete[] R;
}

void mergeSort(int arr[], int l, int r)
{
    if (l < r)
    {
        int m = l + (r - l) / 2;

        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);

        merge(arr, l, m, r);
    }
}

int main()
{

    const string insertionSortFileName = "insertionSort.csv";
    const string mergeSortFileName = "mergeSort.csv";
    const string randomArrayFileName = "randomArrayFile.txt";

    ofstream insertionSortFile(insertionSortFileName);
    ofstream mergeSortFile(mergeSortFileName);

    insertionSortFile << "Array Size,Time (Insertion Sort),Sorted Array" << endl;
    mergeSortFile << "Array Size,Time (Merge Sort),Sorted Array" << endl;
    cout << "Array Size"
         << "\t"
         << "Insertion Time"
         << "\t"
         << "Merge Time"
         << "\t" << endl;

    for (int arraySize = 500; arraySize <= 3000; arraySize += 500)
    {
        int numArray[arraySize];

        generateRandomArray(randomArrayFileName, arraySize);
        readFile(randomArrayFileName, numArray, arraySize);

        // Insertion Sort and measure time
        auto startInsertion = high_resolution_clock::now();
        insertionSort(numArray, arraySize);
        auto stopInsertion = high_resolution_clock::now();
        auto durationInsertion = duration_cast<microseconds>(stopInsertion - startInsertion);
        insertionSortFile << arraySize << "," << durationInsertion.count() << ",";
        for (int i = 0; i < arraySize; ++i)
        { // storing into file
            insertionSortFile << numArray[i] << " ";
        }
        insertionSortFile << endl;

        // Merge Sort and measure time
        auto startMerge = high_resolution_clock::now();
        mergeSort(numArray, 0, arraySize - 1);
        auto stopMerge = high_resolution_clock::now();
        auto durationMerge = duration_cast<microseconds>(stopMerge - startMerge);
        mergeSortFile << arraySize << "," << durationMerge.count() << ",";
        for (int i = 0; i < arraySize; ++i)
        {
            mergeSortFile << numArray[i] << " ";
        }
        mergeSortFile << endl;

        cout << arraySize << "\t\t" << durationInsertion.count() << "\t\t"
             << durationMerge.count() << endl;
    }

    // closing the files where opened
    insertionSortFile.close();
    mergeSortFile.close();

    return 0;
}