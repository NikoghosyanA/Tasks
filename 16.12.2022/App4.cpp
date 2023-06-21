#include <stdio.h>
#include <algorithm>

const int maxn = 100000;

char A[maxn+1][2] = {1};
char index[maxn+2], gray[maxn+2];

void togray(char* gr, char* ind, int n)
{
    for(int i = 0, prev = 0; i < n; i++)
    {
        char x = ind[i] - '0';
        gr[i] = '0' + (x ^ prev);
        prev = x;
    }
}

int main()
{
    int n;
    scanf("%s%n%s", index+1, &n, gray+1);
    for(int i = 1; i <= n; i++)
    {
        char x = index[i]-'0', y = gray[i]-'0';
        if(index[i] == '?')
            if(gray[i] == '?')
                A[i][1] = A[i][0] = A[i-1][0] + A[i-1][1];
            else
                A[i][1] = A[i-1][y^1], A[i][0] = A[i-1][y];
        else
            if(gray[i] == '?')
                A[i][x] = A[i-1][0] + A[i-1][1];
            else
                A[i][x] = A[i-1][y^x];
        A[i][1] = std::min(A[i][1], (char) 2);
        A[i][0] = std::min(A[i][0], (char) 2);
    }
    if(A[n][1] + A[n][0] == 0)
        printf("Impossible");
    else if(A[n][1] + A[n][0] > 1)
        printf("Ambiguity");
    else
    {
        int d = A[n][1] ? '1' : '0';
        for(int i = n; i; i--)
        {
            index[i] = d;
            if(gray[i] == '?')
                d = A[i-1][1] ? '1' : '0';
            else
                d = '0' + (gray[i] != d);
        }
        togray(gray+1, index+1, n);
        printf("%s\n%s", index+1, gray+1);
    }
}
