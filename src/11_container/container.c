#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MIN(X, Y) (((X) < (Y)) ? (X) : (Y))
#define MAX(X, Y) (((X) > (Y)) ? (X) : (Y))

// BruteForce Solution
int solution(int* height, int heightSize){
    int b = 0, h = 0;
    int i = 0, k = (heightSize - 1);
    
    while(i < k){
        for (int l = 0; l <= k; l++)
        {
            int he = abs(l - i);
            int larg = MIN(height[i], height[l]);

            if ((he * larg) > (b * h)){
                b = he;
                h = larg;
            }
        }
        
        i++;
    }

    printf("1: (%d, %d)", h, b);
    return h * b;
}

int Opsolution(int* height, int heightSize){
    int l = 0, r = heightSize - 1;
    int area = 0;

    while (l < r){
        int currentArea = MIN(height[l], height[r]) * (r - l);
        area = MAX(area, currentArea);

        height[l] < height[r] ? l++ : r--;
    }
    return area;
}

int main(){
    int foo[9] = {1,8,6,2,5,4,8,3,7};
    printf("\n %d \n", Opsolution(foo, 9));
    return 0;
}