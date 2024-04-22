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
        Element *max;
        string result = "I'm here";

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
                // finding max element in table;
                if ((*max).val < Matrix[i][j].val)
                {
                    max = &Matrix[i][j];
                }
            }
        }

        // printing

        // Matrix Printing
        cout << endl;
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

        // string Calculaiton
        
        while ((*max).ele != "EX")
        {
            Element *last = (*max).prev;
            if ((*last).ele != (*max).ele)
            {
                result += ((*max).ele);
            }
            max = (*max).prev;
        }
        cout << result;
    }
};

int main()
{
    int i;
    LCSP saharsh("EXPONENTIAL", "POLYNOMIAL");
    saharsh.longestCommonSubSeq();
    cin >> i;
}