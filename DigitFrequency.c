//Probmen Statement:
//Given a string s , consisting of alphabets and digits,
//find the frequency of each digit in the given string.

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
char s[1000];
    int arr[10] = {0};
    scanf("%s",s);
    
    for(int i = 0; i < strlen(s); i ++) {
        int j = s[i] - 48;
        if( j >= 0 && j <= 9 ) {
            arr[j]++;
        }
    }
    
    for(int i = 0; i < 10; i ++) {
        printf("%d ", arr[i]);
    }
    return 0;
    
}
