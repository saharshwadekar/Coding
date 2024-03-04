#include <iostream>
#include <fstream>
#include <time.h>
#include <vector>
#include <random>

using namespace std;

void printArr(const vector<int>& arr, int n, const string& filename) {
    ofstream outputfile(filename);
    for (int i = 0; i < n; i++) {
        outputfile << arr[i] << endl;
    }
    outputfile.close();
}
 
void insertionSort(vector<int>& arr, int n) {
    for (int i = 1; i < n; i++) {
        int j = i - 1;
        int temp = arr[i];
        while (j > -1 && temp < arr[j]) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = temp;
    }
    printArr(arr, n, "insertionSort.txt");
}

void merge(vector<int>& arr, int mid, int lb, int ub) {
    int i = lb;
    int j = mid + 1;
    int k = lb;
    vector<int> arr1(ub - lb + 1);

    while (i <= mid && j <= ub) {
        if (arr[i] < arr[j]) {
            arr1[k - lb] = arr[i];
            k++;
            i++;
        } else {
            arr1[k - lb] = arr[j];
            k++;
            j++;
        }
    }

    while (i <= mid) {
        arr1[k - lb] = arr[i];
        i++;
        k++;
    }

    while (j <= ub) {
        arr1[k - lb] = arr[j];
        k++;
        j++;
    }
 
    for (int i = lb; i <= ub; i++) {
        arr[i] = arr1[i - lb];
    }
}
 
void mergeSort(vector<int>& arr, int lb, int ub) {
    if (lb < ub) {
        int mid = (lb + ub) / 2;
        mergeSort(arr, lb, mid);
        mergeSort(arr, mid + 1, ub);
        merge(arr, mid, lb, ub);
    }
    printArr(arr, arr.size(), "mergeSort.txt");
}
 
void randomNums(int n) {
    vector<int> arr;
    ofstream outputfile("inputprac2.txt");
    for (int i = 0; i < n; i++) {
        outputfile << rand() % n << endl;
    }
    outputfile.close();
}
 
void starter(int n) {
    randomNums(n);
 
    clock_t startTime, endTime;
    double totalTime;
 
    vector<int> arr;
    ifstream readfile("inputprac2.txt");
 
    int value;
    while (readfile >> value) {
        arr.push_back(value);
    }
    readfile.close();
 
    // Insertion Sort
    startTime = clock();
    insertionSort(arr, arr.size());
    endTime = clock();
    totalTime = ((double)(endTime - startTime)) / CLOCKS_PER_SEC;
    cout<<n<<"   "<<totalTime<<"   ";
 
    // Merge Sort
    startTime = clock();
    mergeSort(arr, 0, arr.size() - 1);
    endTime = clock();
    totalTime = ((double)(endTime - startTime)) / CLOCKS_PER_SEC;
    cout<<"   "<<totalTime<<endl;
}
 
int main() {
    starter(500);
    starter(1000);
    starter(1500);
    starter(2000);
    starter(2500);
    starter(3000);
    return 0;
}