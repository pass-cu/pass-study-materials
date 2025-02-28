#include <stdio.h>
#include <stdlib.h>

// 1. Swap two integers using pointers
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b; //Right after this line is executed a 
    *b = temp;
}

// 2. Fill an array with a specific value
void fill_array(int* arr, int n, int value) {
    for (int i = 0; i < n; i++) {
        arr[i] = value; //Right after this line is executed for the 3rd time
    }
}


// 3. Find the maximum value in an array
int find_max(int* arr, int n) {
    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i]; // Right after this line is executed for the 2nd time
        }
    }
    return max;
}

// 4. Reverse an array in place
void reverse_array(int* arr, int n) {
    for (int i = 0, j = n - 1; i < j; i++, j--) {
        swap(&arr[i], &arr[j]); // Right after this line is executed for the 1st time
    }
}

// 5. Copy an array
void copy_array(int* dest, int* src, int n) {
    for (int i = 0; i < n; i++) {
        dest[i] = src[i]; // Right after this line is executed for the 2nd time.
    }
}




int main(void){
  // Inputs for question 1
  // int a = 2;
  // int b = 4;
  // swap(&a,&b);
  // Inputs for question 2
  // int x[5];
  // fill_array(&x,10,2);
  // Inputs for question 3
  // int y[] = {1,2,5,4,3};
  // find_max(&y,5);
  // Inputs for question 4
  //int z[] = {1,2,4,5,6};
  //reverse_array(&z,5);
  // Inputs for question 5
  // int g[] = {5,6,7,8,9};
  // int h[] = {0,1,2,0,2};
  // copy_array(&g,&h,5);
}
