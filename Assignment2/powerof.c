#include <stdio.h>

int powerof(int a, int b) {
    if (b == 0) {
        return 1;
    }
    else {
        return a * powerof(a, b-1);
    }
}

int main () {
    int value = powerof(3, 2);
    printf("%d\n", value);
    return 0;
}
