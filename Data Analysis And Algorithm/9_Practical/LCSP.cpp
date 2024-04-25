#include <bits/stdc++.h>

using namespace std;

struct Element
{
    int val = 0;
    string ele = "EX";
    struct Element *prev = nullptr;
};

class LCSP
{
    string X, Y;
    int xlen, ylen;

public:
    LCSP(string x, string y) : X(x), Y(y)
    {
        xlen = X.length();
        ylen = Y.length();
    }

    void longestCommonSubSeq()
    {
        vector<vector<Element>> Matrix(xlen + 1, vector<Element>(ylen + 1));
        Element *max = &Matrix[0][0];
        string result;

        for (int i = 1; i <= xlen; ++i)
        {
            for (int j = 1; j <= ylen; ++j)
            {
                if (X[i - 1] == Y[j - 1])
                {
                    Matrix[i][j].val = 1 + Matrix[i - 1][j - 1].val;
                    Matrix[i][j].ele = X[i - 1];
                    Matrix[i][j].prev = &Matrix[i - 1][j - 1];
                }
                else if (Matrix[i - 1][j].val < Matrix[i][j - 1].val)
                {
                    Matrix[i][j].val = Matrix[i][j - 1].val;
                    Matrix[i][j].ele = Matrix[i][j - 1].ele;
                    Matrix[i][j].prev = &Matrix[i][j - 1];
                }
                else
                {
                    Matrix[i][j].val = Matrix[i - 1][j].val;
                    Matrix[i][j].ele = Matrix[i - 1][j].ele;
                    Matrix[i][j].prev = &Matrix[i - 1][j];
                }
                if (max->val < Matrix[i][j].val)
                {
                    max = &Matrix[i][j];
                }
            }
        }

        for (int i = 0; i <= xlen; ++i)
        {
            for (int j = 0; j <= ylen; ++j)
            {
                cout << Matrix[i][j].ele << "\t";
            }
            cout << endl;
        }
        cout << endl
             << endl;

        while (max->ele != "EX")
        {
            if (result.empty() || result.back() != max->ele[0])
            {
                result += max->ele;
            }
            max = max->prev;
        }

        reverse(result.begin(), result.end());
        int length = result.size();
        cout << "Longest Common Subsequence: " << result << endl;
        cout << "Length of LCS: " << length << endl;
    }
};

int main()
{
    LCSP saharsh("EXPONENTIAL", "POLYNOMIAL");
    saharsh.longestCommonSubSeq();
    return 0;
}

//Output
PS D:\Coding\Data Analysis And Algorithm> cd "d:\Coding\Data Analysis And Algorithm\9_Practical\" ; if ($?) { g++ LCSP.cpp -o LCSP } ; if ($?) { .\LCSP }
EX      EX      EX      EX      EX      EX      EX      EX      EX      EX      EX
EX      EX      EX      EX      EX      EX      EX      EX      EX      EX      EX
EX      EX      EX      EX      EX      EX      EX      EX      EX      EX      EX
EX      P       P       P       P       P       P       P       P       P       P
EX      P       O       O       O       O       O       O       O       O       O
EX      P       O       O       O       N       N       N       N       N       N
EX      P       O       O       O       N       N       N       N       N       N
EX      P       O       O       O       N       N       N       N       N       N
EX      P       O       O       O       N       N       N       N       N       N
EX      P       O       O       O       N       N       N       I       I       I
EX      P       O       O       O       N       N       N       I       A       A
EX      P       O       L       L       N       N       N       I       A       L


Longest Common Subsequence: PONIAL
Length of LCS: 6