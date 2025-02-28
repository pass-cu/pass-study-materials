#include <stdio.h>
#include <stdlib.h>



int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
// factorial(5)
// return 5 * factorial(4)
// return 5 * 4 * factorial(3)
// return 5 * 4 * 3 * factorial(2)
// return 5 * 4 * 3 * 2 * factorial(1)
// return 5 * 4 * 3 * 2 * 1
// return 120

int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}
// fibonacci(7)

int sum_n(int n) {
    if (n == 0) return 0;
    return n + sum_n(n - 1);
}
// sum_n(8)

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}
// gcd(12,8)

int count_digits(int n) {
    if (n == 0) return 0;
    return 1 + count_digits(n / 10);
}
// count_digits(10025)

int main(void){
}
