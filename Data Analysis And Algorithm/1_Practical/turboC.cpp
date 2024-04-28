#include <iostream.h>
#include <fstream.h>
#include <time.h>
#include <stdlib.h>
#include <conio.h>

void generateRandomArray(const char *fileName, const int size)
{
    ofstream file(fileName);
    if (!file)
    {
        cerr << "ERROR OPENING :" << fileName << endl;
        exit(1);
    }
    srand((unsigned)time(0));
    for (int i = 0; i < size; ++i)
    {
        file << rand() % 1000 << " ";
    }
    file.close();
}

void readFile(const char *fileName, int arr[], int size)
{
    ifstream file(fileName);
    if (!file)
    {
        cerr << "ERROR READING :" << fileName << endl;
        exit(1);
    }
    for (int i = 0; i < size; ++i)
    {
        file >> arr[i];
    }
    file.close();
}

void bubbleSort(int arr[], int size)
{
    for (int i = 0; i < size - 1; ++i)
    {
        int flag = 0;
        for (int j = 0; j < size - i - 1; ++j)
        {
            if (arr[j] > arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                flag = 1;
            }
        }
        if (!flag)
            break;
    }
}

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
        int temp = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = temp;
    }
}

int main()
{
    clrscr();
    const char *inputFile = "inputfile.txt";
    const char *randomArrayFileName = "randomArrayFile.txt";

    int randomSize = (rand() % 10) + 1;
    int *sizeArray = new int[randomSize];

    generateRandomArray(inputFile, randomSize);
    int *numArray = new int[randomSize];
    readFile(inputFile, numArray, randomSize);

    cout << "Array Size\tTime (Bubble Sort)\tTime (Selection Sort)" << endl;

    for (int i = 0; i < randomSize; ++i)
    {
        generateRandomArray(randomArrayFileName, sizeArray[i]);
        readFile(randomArrayFileName, numArray, sizeArray[i]);

        // Bubble Sort and measure time
        clock_t startBubble = clock();
        bubbleSort(numArray, sizeArray[i]);
        clock_t stopBubble = clock();
        double durationBubble = double(stopBubble - startBubble) / CLOCKS_PER_SEC;

        // Selection Sort and measure time
        clock_t startSelection = clock();
        selectionSort(numArray, sizeArray[i]);
        clock_t stopSelection = clock();
        double durationSelection = double(stopSelection - startSelection) / CLOCKS_PER_SEC;

        cout << sizeArray[i] << "\t\t" << durationBubble << "\t\t\t" << durationSelection << endl;
    }

    delete[] sizeArray;
    delete[] numArray;
    getch();
    return 0;
}
